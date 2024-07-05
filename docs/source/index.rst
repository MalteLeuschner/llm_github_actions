.. llm_github_actions documentation master file, created by
   sphinx-quickstart on Fri Jul  5 08:23:30 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to llm_github_actions's documentation!
==============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

========================
Project Title: OCR and Financial Data Management
=======================

Project Description
------------------

This project is a financial data management system that utilizes Optical Character Recognition (OCR) to extract text from image files. The extracted text is then processed and stored in a SQLite database. The project also includes data visualization capabilities to display the financial data in a user-friendly format.

Installation Instructions
-------------------------

To install this project, first ensure that you have Python 3.x installed on your system. You will also need to install the following dependencies:

* `pandas`
* `numpy`
* `Pillow`
* `matplotlib`
* `streamlit`
* `sqlite3`
* `pytesseract`

You can install these dependencies using pip:

.. code-block:: bash

    pip install pandas numpy Pillow matplotlib streamlit sqlite3 pytesseract

Verzeichnisstruktur
-------------------

The project has the following directory structure:

* `ocr_handler.py`: Contains the OCRHandler class responsible for performing OCR on image files.
* `database_handler.py`: Contains the DatabaseHandler class responsible for managing the SQLite database.
* `data_visualizer.py`: Contains the DataVisualizer class responsible for visualizing the financial data.
* `main.py`: The entry point of the application, initializes the OCRHandler, DatabaseHandler, and DataVisualizer classes and performs the necessary operations.

Dateibeschreibungen
-------------------

* `ocr_handler.py`:

    - OCRHandler Class:

        - `__init__(self, tesseract_cmd: str) -> None`: Initializes the OCRHandler instance and sets up the tesseract command for the OCR process.
        - `perform_ocr(self, image_path: str) -> str`: Performs OCR on an image and returns the extracted text.

* `database_handler.py`:

    - DatabaseHandler Class:

        - `__init__(self, db_name: str) -> None`: Initializes a DatabaseHandler instance and creates a connection to the SQLite database.
        - `create_table(self) -> None`: Creates a 'transactions' table in the database if it does not already exist.
        - `insert_transaction(self, date: str, description: str, amount: float) -> None`: Inserts a new transaction into the transactions table.
        - `query_transactions(self) -> List[Tuple[int, str, str, float]]`: Queries all transactions from the database and returns them as a list of tuples.
        - `close(self) -> None`: Closes the database connection.

* `data_visualizer.py`:

    - DataVisualizer Class:

        - `__init__(self, data: Dict[str, List[str]]) -> None`: Initializes a DataVisualizer instance by creating a pandas DataFrame from the provided data.
        - `display_data(self) -> None`: Displays the transaction data in a dataframe using Streamlit.
        - `plot_line_chart(self) -> None`: Generates a line chart of transaction amounts over time using matplotlib and displays it using Streamlit.
        - `plot_bar_chart(self) -> None`: Generates a bar chart of transaction amounts over time using matplotlib and displays it using Streamlit.

Nutzung
-------

To use the project, run the `main.py` script. The script will perform OCR on an image file called "balance\_sheet.png", insert the extracted data into the SQLite database, and display the data using Streamlit.

Beitragende
----------

The project was developed by [Your Name Here].

Lizenz
------

This project is licensed under the [MIT License].

.. [MIT License]: <https://opensource.org/licenses/MIT>