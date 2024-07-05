.. llm_github_actions documentation master file, created by
   sphinx-quickstart on Fri Jul  5 09:46:05 2024.
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


=====================
LLM GitHub Actions
=====================

Project Description
-------------------

The LLM GitHub Actions project consists of three main scripts that perform different functionalities. The first script, `OCRHandler`, is used to perform Optical Character Recognition (OCR) on an image using the `pytesseract` library. The script contains a single class, `OCRHandler`, and a `main` function that demonstrates its usage. The `OCRHandler` class has two methods: `__init__` and `perform_ocr`. The `__init__` method initializes the `OCRHandler` instance by setting the path to the Tesseract command-line tool, while the `perform_ocr` method performs OCR on an image and returns the extracted text as a string.

The second script is a simple program that uses SQLite to manage financial transactions. It contains a single class, `DatabaseHandler`, and a `main` function. The `DatabaseHandler` class is responsible for handling database operations, such as creating a connection to a SQLite database, creating a table for transactions if it doesn't exist, inserting transactions, querying existing ones, and closing the database connection.

The third script consists of a main function and a `DataVisualizer` class. The `DataVisualizer` class is used to represent and visualize financial data. It is initialized with a dictionary containing the dataset, which is then converted into a pandas DataFrame for further processing. The `DataVisualizer` class has three methods: `display_data`, `plot_line_chart`, and `plot_bar_chart`. These methods display the transaction data in a Streamlit dataframe, generate a line chart using matplotlib, and generate a bar chart using the provided data, respectively.

Installation Instructions
-------------------------

To install the LLM GitHub Actions project, first clone the repository using the following command:

.. code-block:: bash

   git clone https://github.com/username/llm_github_actions.git

Next, navigate to the project directory and install the required dependencies using pip:

.. code-block:: bash

   cd llm_github_actions
   pip install -r requirements.txt

File Descriptions
-----------------

- `ocr.py`: Contains the `OCRHandler` class and `main` function for performing OCR on an image.
- `database.py`: Contains the `DatabaseHandler` class and `main` function for managing financial transactions using SQLite.
- `data_visualization.py`: Contains the `DataVisualizer` class and `main` function for visualizing financial data.

Usage
-----

To use the `OCRHandler` script, simply run the `ocr.py` file and provide the path to an image file as a command-line argument:

.. code-block:: bash

   python ocr.py image.png

To use the `DatabaseHandler` script, run the `database.py` file and provide the path to the SQLite database file as a command-line argument:

.. code-block:: bash

   python database.py database.db

To use the `DataVisualizer` script, run the `data_visualization.py` file and provide the path to the financial dataset as a command-line argument:

.. code-block:: bash

   python data_visualization.py dataset.json

Contributors
------------

- John Doe
- Jane Smith

License
-------

This project is licensed under the MIT License.