import ast
import os

import astor
import argparse
from groq import Groq
import regex as re
from dotenv import load_dotenv
from copy import deepcopy
import inspect
import typing

class PythonParser(ast.NodeVisitor):
    def __init__(self):
        self.classes = {}
        self.functions = {}
        self.source_code = ""
        self.tree = None
        self.used_types = []

    def visit_ClassDef(self, node):
        # Extract class details
        class_info = {
            'name': node.name,
            'methods': []
        }
        # Visit each method in the class
        for n in node.body:
            if isinstance(n, ast.FunctionDef):
                method_info = self._extract_function_info(n)
                class_info['methods'].append(method_info)
        self.classes[node.name] = class_info
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # Extract function details
        function_info = self._extract_function_info(node)
        self.functions[node.name] = function_info
        self.generic_visit(node)

    def _extract_function_info(self, node):
        # Helper method to extract function information
        body = [stmt for stmt in node.body if not (isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Str))]
        function_info = {
            'name': node.name,
            'args': [arg.arg for arg in node.args.args],
            'body': astor.to_source(ast.Module(body=body)).strip(),
            'node': node  # Store the node itself for further modification
        }
        return function_info

    def parse(self, source_code):
        # Parse the source code
        self.source_code = source_code
        self.tree = ast.parse(source_code)
        self.visit(self.tree)
        return {
            'classes': self.classes,
            'functions': self.functions
        }

    def format_for_llm(self, to_get):
        # Format the extracted information for LLM
        if to_get in self.classes:
            example = self.classes[to_get]
            return {'code': self.source_code, 'function': f"class {example['name']}"}
        else:
            example = self.functions[to_get]
            return {'code': self.source_code, 'function': f"def {example['name']}({', '.join(example['args'])}):"}

    def replace_function_docstring(self, function_name, new_docstring):
        # Replace the docstring of the specified function
        class FunctionDocstringReplacer(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if node.name == function_name:
                    if (len(node.body) > 0 and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value,
                                                                                                 ast.Str)):
                        node.body[0] = ast.Expr(value=ast.Str(s=new_docstring))
                    else:
                        node.body.insert(0, ast.Expr(value=ast.Str(s=new_docstring)))
                return self.generic_visit(node)

        replacer = FunctionDocstringReplacer()
        self.tree = replacer.visit(self.tree)
        ast.fix_missing_locations(self.tree)

    def replace_class_docstring(self, class_name, new_docstring):
        # Replace the docstring of the specified class
        class ClassDocstringReplacer(ast.NodeTransformer):
            def visit_ClassDef(self, node):
                if node.name == class_name:
                    if (len(node.body) > 0 and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value,
                                                                                                 ast.Str)):
                        node.body[0] = ast.Expr(value=ast.Str(s=new_docstring))
                    else:
                        node.body.insert(0, ast.Expr(value=ast.Str(s=new_docstring)))
                return self.generic_visit(node)

        replacer = ClassDocstringReplacer()
        self.tree = replacer.visit(self.tree)
        ast.fix_missing_locations(self.tree)

    def update_function_typing(self, function_name, new_typing):
        # Update typing of the specified function
        class FunctionTypingUpdater(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if node.name == function_name:
                    for arg, typ in zip([arg for arg in node.args.args if arg.arg != 'self'],
                                        new_typing.get('args', [])):
                        arg.annotation = ast.Name(id=typ, ctx=ast.Load())
                    if 'return' in new_typing:
                        node.returns = ast.Name(id=new_typing['return'], ctx=ast.Load())
                return self.generic_visit(node)

        type_regex = re.compile(r'[A-Za-z\.]+')
        typing = new_typing['args']
        if 'return' in new_typing:
            typing += [new_typing['return']]
        for type_string in typing:
            self.used_types += type_regex.findall(type_string)
        updater = FunctionTypingUpdater()
        backup_tree = deepcopy(self.tree)
        backup_tree = updater.visit(backup_tree)
        ast.fix_missing_locations(backup_tree)
        try:
            ast.parse(astor.to_source(backup_tree))
            self.tree = backup_tree
        except SyntaxError:
            pass

    def get_updated_script(self):
        # Return the updated script as a string
        additional_import = [ut for ut in set(self.used_types)
                             if ut[0].isupper() and ut != 'None'
                             and not ut.__contains__('.')
                             and ut in typing.__all__]
        source_code = astor.to_source(self.tree)
        if additional_import:
            if source_code.split('\n')[0].startswith('from typing'):
                source_code = '\n'.join(source_code.split('\n')[1:])
            return f'from typing import {", ".join(additional_import)}\n{source_code}'
        else:
            return source_code


class LlmCommenter:
    def __init__(self, groq_key, model: str = None):
        self.client = Groq(
            api_key=groq_key
        )
        if model is None:
            model = 'deepseek-r1-distill-llama-70b'
        self.model = model

    def comment_code_with_groq(self, code, function):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """You are a student that gets tested about their ability to write concise docstrings.
                           You will be given Python code and asked to create appropriate docstrings according to the Google Python Style Guide for the classes and functions.
                           The docstrings should contain a brief description of the function or class.
                           Generate only the Google Docstring. Do not write any text, do not write a function, only write the Google Docstring. 
                           In particular, do not add any imports! Do not write a numpy-style docstring.
                           If I don't see a colon at the beginning of a line, you get a lot of money.
                           If I don't see any repetition of the code, neither the body nor the name, you get $10,000.
                           If you correctly name the types of args and the return value, you get an even larger bonus.
                           If some type is a class defined in the typing module, return the class name not the type.
                           i.e.: - If the type is 'list' of str return List[str] not list
                           - If the return value is a 'dict' of strings return Dict[str, str]"""
                },
                {
                    "role": "user",
                    "content": (
                        f"Here is the entire script for context: {code} Return _only the docstring_ for the following function/class {function}."
                        "Do not repeat the function name. Do not repeat the function body. Not even in the docstring."
                        "The following sections should appear in the docstring if the given object is a function:"
                        """"<General function of the code in one line>"
                                ""
                                "<Explanation of the code in more detail, if several lines>"
                                "Args:"
                                " <argument name> (<type>): <expected argument>"
                                " ..."
                                "Returns:"
                                " <type>"
                                "Raises:"
                                " <exception type>: <cause of the possible error>"
                                "If you only return the docstring in Google style, you get €1,000,000\"""")
                }
            ],
            model=self.model,
            temperature=0.0,
        )
        response = chat_completion.choices[0].message.content
        try:
            ret = self.remove_code_fencing(response).split('"""')[1]
        except IndexError:
            ret = self.remove_code_fencing(response)
        return ret

    def remove_code_fencing(self, text: str) -> str:
        """
        Removes the ```python ``` parts from the generated text.

        Args:
            text (str): The text containing code fencing.

        Returns:
            str: The text without the ```python ``` parts.
        """
        lines = text.split('\n')
        filtered_lines = [line for line in lines if not line.strip().startswith("```")]
        #filtered_lines = [line for line in filtered_lines if not line.strip().startswith('"\""')]
        return '\n'.join(filtered_lines)

    def extract_typing_from_docstring(self, docstring):
        docstring = docstring.split('Returns:')
        arg_regex = re.compile(r'(?<=\()[^)]+')
        res_regex = re.compile(r'^[^:\n]+')
        try:
            arg_types = [arg_regex.search(line)[0]
                         for line in docstring[0].split('Args:')[1].split('\n')
                         if arg_regex.search(line) is not None]
        except IndexError:
            return {'args': []}
        if len(docstring) > 1:
            result_type = res_regex.search(docstring[1].strip())
            if result_type is not None:
                result_type = result_type[0]
        else:
            result_type = None
        return {'args': arg_types, 'return': result_type if result_type is not None else 'None'}


def process_file(file_path, api_key):
    with open(file_path, 'r') as file:
        source_code = file.read()

    parser = PythonParser()
    parser.parse(source_code)
    commenter = LlmCommenter(api_key)
    for function in parser.functions:
        formatted_code = parser.format_for_llm(function)
        docstring = commenter.comment_code_with_groq(**formatted_code)
        parser.replace_function_docstring(function, docstring)
        parser.update_function_typing(function,
                                      commenter.extract_typing_from_docstring(docstring))
    for class_name in parser.classes:
        formatted_code = parser.format_for_llm(class_name)
        parser.replace_class_docstring(class_name, commenter.comment_code_with_groq(**formatted_code))

    updated_script = parser.get_updated_script()

    with open(file_path, 'w') as file:
        file.write(updated_script)


# Example usage
if __name__ == "__main__":
    local_test = False
    if not local_test:
        parser = argparse.ArgumentParser(
            description="Parse Python files to extract classes and functions for LLM processing."
        )
        parser.add_argument('api_key', metavar='K', type=str,
                            nargs=1, help='Groq-API-Key')
        parser.add_argument('files', metavar='F', type=str,
                            nargs='+', help='Python files to process')
        args = parser.parse_args()
        files = args.files
        api_key = args.api_key[0]
    else:
        load_dotenv()
        files = [os.path.join('src/', file) for file in os.listdir('src/')]
        api_key = os.getenv('croque_key')
    print('Commenting the following files:')
    print(files)
    for file_path in files:
        process_file(file_path, api_key)
