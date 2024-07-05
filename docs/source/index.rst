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

The OCRHandler class
====================

The OCRHandler class is initialized with a tesseract command path. This class is responsible for handling OCR operations using the pytesseract library.

Args:
tesseract\_cmd (str): The path to the tesseract command.

Methods:

* **\_\_init\_\_(self, tesseract\_cmd: str) -> None**:
Initializes the OCRHandler instance and sets the tesseract command for the pytesseract library.

* **perform\_ocr(self, image\_path: str) -> str**:
Performs Optical Character Recognition (OCR) on an image. This function uses the pytesseract library to extract text from an image.

Args:
image\_path (str): The path to the image file.

Returns:
str: The extracted text from the image.

Raises:
FileNotFoundError: If the image file does not exist.

Main Function:
The main function initializes an OCRHandler instance with the path to the tesseract command and performs OCR on an image file named "balance\_sheet.png". The extracted text is then printed.

Args:
None

Returns:
None

Raises:
None

.. DatabaseHandler Class

The DatabaseHandler class
=======================

The DatabaseHandler class is a database handler class that manages the interaction with an SQLite database. It creates a table for transactions, inserts transactions, queries transactions, and closes the database connection.

The class has five methods:

1. **__init__(self, db\_name: str) -> None**:
Initializes a DatabaseHandler object by creating a connection to an SQLite database and initializing a cursor object.

2. **create\_table(self) -> None**:
Creates a table in the database if it does not exist. The table named 'transactions' has columns 'id', 'date', 'description', and 'amount'.

3. **insert\_transaction(self, date: str, description: str, amount: float) -> None**:
Inserts a transaction into the database by executing a SQL query.

4. **query\_transactions(self) -> List[Tuple]**:
Retrieves all transactions from the database by executing a SQL query and returns the result as a list of tuples.

5. **close(self) -> None**:
Closes the database connection.

Main Function:
The main function runs the entire program by creating a DatabaseHandler object, inserting a transaction, querying all transactions, and printing them. The database file is named "financial\_data.db". The transaction inserted has a date of "2024-07-05", a description of "Deposit", and an amount of 1000.0. The program then prints all the transactions in the database and closes the database connection.

.. DataVisualizer Class

The DataVisualizer class
=======================

The DataVisualizer class is designed for visualizing transaction data. It creates a pandas DataFrame from the provided data for further visualization.

- **__init__(self, data: Dict[str, List[str]]) -> None**:
This constructor initializes a DataVisualizer instance and creates a pandas DataFrame from the provided data.

- **display\_data(self) -> None**:
This method displays the transaction data in a dataframe using Streamlit's dataframe function.

- **plot\_line\_chart(self) -> None**:
This method generates a line chart using matplotlib, where the x-axis represents the date and the y-axis represents the amount. The chart is then displayed using Streamlit's pyplot function.

- **plot\_bar\_chart(self) -> None**:
This method generates a bar chart using the provided data, with dates on the x-axis and amounts on the y-axis. The chart is then displayed using Streamlit's pyplot function.

main() Function:
The main function initializes the DataVisualizer class with sample data, sets the Streamlit title, and displays the dataframe, line chart, and bar chart.

Program Flow:

1. The script initializes the DataVisualizer class with a dictionary containing transaction data.
2. The Streamlit title is set to "Financial Data Visualization".
3. The display\_data method is called to display the transaction data in a dataframe.
4. The plot\_line\_chart method is called to generate and display a line chart of transaction amounts over time.
5. The plot\_bar\_chart method is called to generate and display a bar chart of transaction amounts over time.

.. Projektinstallation:

Installation instructions:
---------------------------

1. Clone the repository:

   ```
   git clone https://github.com/username/repository.git
   ```

2. Navigate to the project directory:

   ```
   cd repository
   ```

3. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

5. Run the program:

   ```
   python main.py
   ```

Required packages:
------------------

* pytesseract
* opencv-python-headless
* pandas
* matplotlib
* streamlit
* sqlite3

.. Projektstruktur:

Verzeichnisstruktur:
---------------------

* repository/

  * data/
  * docs/
  * financial\_data.db
  * financial\_data.png
  * main.py
  * requirements.txt
  * OCRHandler.py
  * DatabaseHandler.py
  * DataVisualizer.py

.. Nutzung:

Usage:
------

1. Run the program:

   ```
   python main.py
   ```

2. Follow the instructions in the Streamlit interface.

.. Beitragende:

Contributors:
-------------

* [Your Name](mailto:you@example.com)

.. Lizenz:

License:
-------

This project is licensed under the MIT License - see the LICENSE.md file for details.