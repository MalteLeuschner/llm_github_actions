import ast
import astor
import sys
import argparse

class PythonParser(ast.NodeVisitor):
    def __init__(self):
        self.classes = {}
        self.functions = {}
        self.source_code = ""
        self.tree = None

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
            return (self.source_code, f"class {example['name']}")
        else:
            example = self.functions[to_get]
            return (self.source_code, f"def {example['name']}({', '.join(example['args'])}):\n    {example['body']}")

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
                    for arg, typ in zip(node.args.args, new_typing.get('args', [])):
                        arg.annotation = ast.Name(id=typ, ctx=ast.Load())
                    if 'return' in new_typing:
                        node.returns = ast.Name(id=new_typing['return'], ctx=ast.Load())
                return self.generic_visit(node)

        updater = FunctionTypingUpdater()
        self.tree = updater.visit(self.tree)
        ast.fix_missing_locations(self.tree)

    def get_updated_script(self):
        # Return the updated script as a string
        return astor.to_source(self.tree)


def ds_dummy(context, function):
    return """
    This is an example Docstring
    
    Args:
        a: an arg
        
    Returns:
        b: some results
    
    Example:
        A very good Example.
"""


def process_file(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    parser = PythonParser()
    parser.parse(source_code)
    for function in parser.functions:
        formatted_code = parser.format_for_llm(function)
        parser.replace_function_docstring(function, ds_dummy(*formatted_code))
    for class_name in parser.classes:
        formatted_code = parser.format_for_llm(class_name)
        parser.replace_class_docstring(class_name, ds_dummy(*formatted_code))

    # # Example: Update typing of a function (example, this should be done by LLM and then passed here)
    # parser.update_function_typing("example_function",
    #                               {'args': ['int', 'str'], 'return': 'None'})
    #
    updated_script = parser.get_updated_script()
    # print(f"\nUpdated Script from {file_path}:\n", updated_script)

    # Write the updated script back to the file
    with open(file_path, 'w') as file:
        file.write(updated_script)

# Example usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse Python files to extract classes and functions for LLM processing."
    )
    parser.add_argument('files', metavar='F', type=str, nargs='+', help='Python files to process')
    args = parser.parse_args()

    for file_path in args.files:
        process_file(file_path)
