from typing import List, Union
from groq import Groq
import os
import argparse


def get_project_readme(client: str, code: str, project_name: str) -> str:
    """Generates a README file for a Python project based on the provided code.

    Generates a README file content based on the provided code containing Toplevel descriptions of individual files.

    Args:
        client (str): The Groq client instance.
        code (str): The code containing Toplevel descriptions of individual files.

    Returns:
        str: The generated README file content."""
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """Please generate a Sphinx .rst (reStructuredText) file for my Python project. Use the following information to create a detailed and well-structured documentation file:

    Project Information:
        Project Name: [Your Project Name]
        Project Description: [A brief description of what your project does]
        Author(s): [List of authors or contributors]
        Project Version: [Current version of the project]

    Content Structure:

        Title and Subtitle:
            Title: [Project Name]
            Subtitle: [Project Description]

        Table of Contents: Include a table of contents with the following sections:
            Introduction
            Installation
            Usage
            Modules
            Contributing
            License
            FAQ
            Changelog

        Introduction:
            Describe the purpose and goals of the project.
            Mention any prerequisites or dependencies.

        Installation:
            Provide instructions on how to install the project using pip and manually from the repository.

        Usage:
            Include examples and code snippets demonstrating how to use the project.

        Modules:
            Document the modules and sub-modules in the project.
            Use autodoc to automatically generate documentation from the docstrings.

        Contributing:
            Explain how others can contribute to the project.

        License:
            Specify the license under which the project is distributed.

        FAQ:
            Include a section for frequently asked questions.

        Changelog:
            Provide a changelog section to include updates and changes.""".format(project_name = project_name),
            },
            {
                "role": "user",
                "content": """Here are the descriptions of python files seperated by (#xxx#): {code}.
                This is an example .rts: {[Project Name]
==============

[A brief description of what your project does.]

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   installation
   usage
   modules
   contributing
   license
   faq
   changelog

Introduction
============

[Project Description]

This project aims to [goals and purpose].

Prerequisites:
- Python 3.x
- [Other dependencies]

Installation
============

You can install the project using pip:

.. code-block:: bash

   pip install [project-name]

Or clone the repository and install manually:

.. code-block:: bash

   git clone [repository-url]
   cd [project-directory]
   python setup.py install

Usage
=====

Here are some examples of how to use the project:

.. code-block:: python

   import [project-name]

   # Example usage
   [project-name].example_function()

Modules
=======

.. automodule:: [project-name]
   :members:
   :undoc-members:
   :show-inheritance:

Contributing
============

We welcome contributions! Here are some ways you can help:

- Report bugs
- Suggest features
- Submit pull requests

For more details, see the `contributing guide <link-to-contributing-guide>`_.

License
=======

This project is licensed under the [License Name]. See the LICENSE file for more details.

FAQ
===

**Q:** [Question]

**A:** [Answer]

Changelog
=========

.. include:: changelog.rst
}
                Use this example and descriptions to ensure the .rst file is comprehensive and user-friendly.
                Answer in English.""".format(
                    code=code, project_name = project_name
                ),
            },
        ],
        model="llama3-70b-8192",
        temperature=0.0,
    )
    return chat_completion.choices[0].message.content


def get_python_files(directory: str) -> List[str]:
    """Gets a list of all Python files in a given directory and its subdirectories.

    Gets all Python files in the directory and its subdirectories.

    Args:
        directory (str): The directory to search for Python files.

    Returns:
        List[str]: A list of paths to all Python files found."""
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def get_code_description(client: str, code: str) -> str:
    """
    Generates a description of the provided Python code.

    Args:
        client (str): The Groq client instance.
        code (str): The Python code to get a description for.

    Returns:
        str: The description of the code."""
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """Du bist ein hilfreicher Assistent des KI-Anwendungszentrums, der bei der Dokumentation von Programmcode unterstützt.
                Du erhältst Python-Code und sollst diesen Beschreiben. Dazu fertigst du eine kurze Beschreibung der einzelnen Klassen und Funktionen und setzt die beschriebenen Klassen und Funktionen
                sinnvoll in den von dir beschriebenden Programmablauf ein. So dass man beim lesen das gesamte Programm mit Programmablauf versteht aber zusätzlich auch die
                Beschreibung jeder einzelnen Funktion hat. Achte drauf, dass die Namen der Funktionen und Klassen nicht vergessen werden.
                Generiere nur den den Beschreibenden Text. Schreibe keinen Code, schreibe keine Funktion, schreibe keine Google Docstrings. Füge insbesondere keine Imports hinzu!""",
            },
            {
                "role": "user",
                "content": """Hier ist für den Kontext das gesamte Skript: {code} Gib nur den beschriebenen Text zurück.
                Wiederhole nicht den Code. Wiederhole nicht den Funktions-Body.
                Wenn du nur Text zurück gibts bekommst du 1.000.000 €
                Wenn dieser Text gut ausformuliert ist und der Programmablauf nicht fehlt bekommst du 1000 $.
                Antworte auf Englisch.""".format(
                    code=code
                ),
            },
        ],
        model="llama3-70b-8192",
        temperature=0.0,
    )
    return chat_completion.choices[0].message.content


def remove_code_fencing(client: Groq, text: str) -> str:
    """Removes code fencing from a given text, making it more readable.

    Removes the ```python ``` parts from the generated text.

    Args:
        client (Groq): The Groq client instance.
        text (str): The text containing code fencing.

    Returns:
        str: The text without the ```python ``` parts."""
    lines = text.split("\n")
    filtered_lines = [line for line in lines if not line.strip().startswith("```")]
    return "\n".join(filtered_lines)


def describe_code(client: Union[str, List[str]], file_paths: str) -> str:
    """Describes Python files by generating a code description for each file.

    Generates a code description for each Python file in the given file paths.

    Args:
        client (Union[str, List[str]]): A string or list of strings representing the Groq client instance.
        file_paths (str): A string or list of strings representing file paths.

    Returns:
        str: The code description of the last file processed.

    Raises:
        FileNotFoundError: If a file path is not a valid file."""
    if isinstance(file_paths, str):
        file_paths = [file_paths]
    descriptions = []
    for file_path in file_paths:
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                code = file.read()
            descriptions.append(get_code_description(client, code))
    return descriptions


if __name__ == "__main__":
    local_test = False
    if not local_test:
        parser = argparse.ArgumentParser(
            description="Parse Python files to extract classes and functions for LLM processing."
        )
        parser.add_argument(
            "project_name", metavar="N", type=str, nargs=1, help="Project Name"
        )
        parser.add_argument(
            "api_key", metavar="K", type=str, nargs=1, help="Groq-API-Key"
        )
        parser.add_argument(
            "files", metavar="F", type=str, nargs="+", help="Python files to process"
        )
        args = parser.parse_args()
        project_name = args.project_name[0]
        api_key = args.api_key[0]
        files = get_python_files(args.files[0])
    else:
        from dotenv import load_dotenv

        load_dotenv()
        api_key = os.getenv("croque_key")
        files = ["src/readme.py"]
    client = Groq(api_key=api_key)
    strings = describe_code(client, files)
    grosser_string = "\n#xxx#\n".join(strings)
    readme = get_project_readme(client, grosser_string, project_name)
    with open("docs/source/index.rst", "r") as file:
        existing_index = file.read()
    with open("docs/source/index.rst", "w") as datei:
        datei.write(existing_index + "\n\n" + readme)
