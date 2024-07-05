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

The OCRHandler class is initialized with the path to the Tesseract command. It has an **init** method that sets up the Tesseract command for the OCR process. The class also has a perform\_ocr method that performs Optical Character Recognition (OCR) on an image, reads the text in it using the Tesseract OCR engine, and returns the extracted text.

**Args:**

* tesseract\_cmd (str): The path to the Tesseract command.
* image\_path (str): The path to the image file.

**Returns:**

* None for **init** method.
* str: The extracted text from the image for perform\_ocr method.

**Raises:**

* IOError: If the image file cannot be opened for perform\_ocr method.

.. DatabaseHandler Klasse

The DatabaseHandler Klasse enables interaction with an SQLite database. It has a number of methods to create a table, insert transactions, retrieve all transactions, and close the database connection.

* The **init** constructor creates a database connection and initializes the cursor. It also creates the transactions table if it does not already exist.
* The create\_table method creates the transactions table in the database.
* The insert\_transaction method inserts a new transaction into the database.
* The query\_transactions method retrieves all transactions from the database and returns them as a list of tuples.
* The close method closes the database connection.

.. DataVisualizer Class

The DataVisualizer class is designed for visualizing financial data. It takes in a dictionary containing 'Date' and 'Amount' data. If the input data is not in the correct format, a ValueError is raised.

The DataVisualizer class has three methods:

1. display\_data(): This method displays the transaction data in a dataframe. It is used to show the transaction data in a tabular format for the user to view.
2. plot\_line\_chart(): This method plots a line chart of transaction amounts over time. It generates a line chart using matplotlib, where the x-axis represents the date and the y-axis represents the amount. The chart is then displayed using streamlit. If the dataframe is empty or does not contain the required columns, a ValueError is raised.
3. plot\_bar\_chart(): This method displays a bar chart of transaction amounts over time. It generates a bar chart using the provided data, with dates on the x-axis and amounts on the y-axis. If the data is not in the correct format, a ValueError is raised.

.. Main Function

The main function of the script runs the entire data visualization process. It first defines a dictionary containing transaction data. Then, it creates a DataVisualizer instance with the transaction data. The main function then sets the title of the streamlit app and displays the transaction data, line chart, and bar chart using the DataVisualizer methods.

.. Program Ablauf

The script initializes by importing necessary libraries. Then, the DataVisualizer class is defined with its methods. The main function creates a dictionary containing transaction data, creates a DataVisualizer instance, sets the title of the streamlit app, and displays the transaction data, line chart, and bar chart using the DataVisualizer methods. Finally, the script runs the main function if it is being run as the main module.

.. Installation

To install the project, clone the repository and run the following command:

.. code-block:: bash

pip install -r requirements.txt

The project requires the following dependencies:

* Tesseract
* Pillow
* SQLite
* Matplotlib
* Streamlit

.. Verzeichnisstruktur

The project has the following directory structure:

* root
	+ ocr\_handler.py
	+ database\_handler.py
	+ data\_visualizer.py
	+ main.py
	+ requirements.txt

.. Nutzung

The project can be used as follows:

1. Initialize an instance of the OCRHandler class with the path to the Tesseract command.
2. Use the perform\_ocr method to extract text from an image file.
3. Initialize an instance of the DatabaseHandler class with the path to the SQLite database.
4. Use the insert\_transaction method to insert transactions into the database.
5. Use the query\_transactions method to retrieve all transactions from the database.
6. Initialize an instance of the DataVisualizer class with the transaction data.
7. Use the display\_data method to display the transaction data in a tabular format.
8. Use the plot\_line\_chart method to plot a line chart of transaction amounts over time.
9. Use the plot\_bar\_chart method to display a bar chart of transaction amounts over time.

.. Beitragende

The project was contributed to by:

* [Your Name]

.. Lizenz

This project is licensed under the [MIT License].