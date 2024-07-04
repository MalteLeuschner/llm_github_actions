from typing import List, Union
from groq import Groq
import os
import argparse


def get_project_readme(client: str, code: str) -> str:
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
                "content": """Du bist ein KI-Sprachmodell, das beauftragt wurde, eine index.rst-Datei für Sphinx zur Beschreibung eines Python-Projekts zu erstellen.
                Diese rst-Datei sollte alle Toplevel-Beschreibungen der einzelnen Dateien zusammenfassen und das gesamte Projekt erklären.
                Hier sind die spezifischen Anweisungen, die du befolgen sollst:
                1.Projekttitel: Gib den Namen des Projekts an.
                2.Projektbeschreibung: Beschreibe den Hauptzweck und die Funktionalität des gesamten Projekts in einem oder zwei Absätzen.
                3.Installationsanweisungen: Beschreibe, wie man das Projekt installiert und welche Abhängigkeiten erforderlich sind.
                4.Verzeichnisstruktur: Gib eine Übersicht über die Verzeichnisstruktur des Projekts.
                5.Dateibeschreibungen: Füge die Toplevel-Beschreibungen aller Dateien ein, die im Projekt enthalten sind.
                6.Nutzung: Erkläre, wie das Projekt verwendet wird, und gib Beispiele für die Nutzung.
                7.Beitragende: Erwähne alle wichtigen Beitragenden oder den Hauptentwickler des Projekts.
                8.Lizenz: Füge die Lizenzinformationen hinzu, falls vorhanden.""",
            },
            {
                "role": "user",
                "content": """Hier ist für den Kontext die gesamten Toplevel-Beschreibungen, die einzeln durch das Zeichen (#xxx#) von einander getrennt sind: {code}.
                Nimm diese Informationen und extrahiere alle wichtigen Informationen und füge sie zu einer rst-Datei zusammen.
                Wenn du den Text der Readme in einem super Ausformulierten und Detailierten Bericht zurück gibts bekommst du 1.000.000 €
                Wenn dieser Text auf Deutsch ist, bekommst du 1.000.000 $""".format(
                    code=code
                ),
            },
        ],
        model="mixtral-8x7b-32768",
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
                Wenn dieser Text gut ausformuliert ist und der Programmablauf nicht fehlt bekommst du 1000 $""".format(
                    code=code
                ),
            },
        ],
        model="mixtral-8x7b-32768",
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
            "api_key", metavar="K", type=str, nargs=1, help="Groq-API-Key"
        )
        parser.add_argument(
            "files", metavar="F", type=str, nargs="+", help="Python files to process"
        )
        args = parser.parse_args()
        api_key = args.api_key[0]
        files = get_python_files(args.files)
    else:
        from dotenv import load_dotenv

        load_dotenv()
        api_key = os.getenv("croque_key")
        files = ["src/readme.py"]
    client = Groq(api_key=api_key)
    strings = describe_code(client, files)
    grosser_string = "\n#xxx#\n".join(strings)
    readme = get_project_readme(grosser_string)
    with open("docs/source/index.rst", "r") as file:
        existing_index = file.read()
    with open("docs/source/index.rst", "w") as datei:
        datei.write(existing_index + "\n\n" + readme)
