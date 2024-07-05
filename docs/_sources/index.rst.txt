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

.. OCRHandler Class

The OCRHandler class is the primary component for performing Optical Character Recognition (OCR) on images. It is initialized with the path to the Tesseract command. The class has an `__init__` method that sets up the Tesseract command for the OCR process. The class also has a `perform_ocr` method that performs OCR on an image, reads the text in it using the Tesseract OCR engine, and returns the extracted text.

Args:
tesseract_cmd (str): The path to the Tesseract command.
image_path (str): The path to the image file.

Returns:
None for `__init__` method.
str: The extracted text from the image for `perform_ocr` method.

Raises:
IOError: If the image file cannot be opened for `perform_ocr` method.

.. DatabaseHandler Klasse

The DatabaseHandler class enables interaction with an SQLite database. It has several methods for creating a table, inserting transactions, retrieving all transactions, and closing the database connection.

- The constructor `__init__` creates a database connection and initializes the table schema.
- The method `create_table` creates a "transactions" table if it does not already exist.
- The method `insert_transaction` inserts a new transaction with the given values into the table.
- The method `query_transactions` executes a SQL query to retrieve all transactions from the table and returns them as a list of tuples.
- The method `close` closes the database connection.

main Funktion:

The main function is the primary function of the program. It creates an object of the DatabaseHandler class, performs a transaction, retrieves all transactions, and prints them.

- The function creates an object of the DatabaseHandler class with the database name "financial_data.db".
- The function performs a transaction with the date "2024-07-05", the description "Deposit", and the amount 1000.0.
- The function retrieves all transactions from the database and prints them as a list of tuples.
- The function closes the database connection.

.. DataVisualizer Class

The DataVisualizer class is designed for visualizing financial data. It takes a dictionary containing 'Date' and 'Amount' data. If the input data is not in the correct format, a ValueError is raised.

The DataVisualizer class has three methods:

1. display_data(): This method displays the transaction data in a dataframe. It is used to show the transaction data in a tabular format for the user to view.

2. plot_line_chart(): This method plots a line chart of transaction amounts over time. It generates a line chart using matplotlib, where the x-axis represents the date and the y-axis represents the amount. The chart is then displayed using streamlit. If the dataframe is empty or does not contain the required columns, a ValueError is raised.

3. plot_bar_chart(): This method displays a bar chart of transaction amounts over time. It generates a bar chart using the provided data, with dates on the x-axis and amounts on the y-axis. If the data is not in the correct format, a ValueError is raised.

Main Function:

The main function of the script runs the entire data visualization process. It first defines a dictionary containing transaction data. Then, it creates a DataVisualizer instance with the transaction data. The main function then sets the title of the streamlit app and displays the transaction data, line chart, and bar chart using the DataVisualizer methods.

Program Ablauf:

The script initializes by importing necessary libraries. Then, the DataVisualizer class is defined with its methods. The main function creates a dictionary containing transaction data, creates a DataVisualizer instance, sets the title of the streamlit app, and displays the transaction data, line chart, and bar chart using the DataVisualizer methods. Finally, the script runs the main function if it is being run as the main module.

Installation:

To install the project, clone the repository and install the required packages using pip:

.. code-block:: bash

   pip install -r requirements.txt

Usage:

To use the project, run the main script:

.. code-block:: bash

   python main.py

Contributors:

- [Your Name]

License:

This project is licensed under the [MIT License].