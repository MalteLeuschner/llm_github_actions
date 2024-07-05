.. llm_github_actions documentation master file, created by
   sphinx-quickstart on Fri Jul  5 09:28:12 2024.
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
====================

Project Description
--------------------

The LLM GitHub Actions project is a collection of Python scripts that demonstrate the use of various libraries and techniques for optical character recognition (OCR), financial database management, and data visualization. The project consists of three main scripts, each focusing on a specific aspect of these functionalities.

The first script, `ocr_script.py`, uses the `pytesseract` library to extract text from an image. It defines a single class, `OCRHandler`, which encapsulates the functionality of performing OCR, making it reusable and easy to integrate into other applications.

The second script, `finance_script.py`, is a simple financial database manager that utilizes SQLite to store and manage financial transactions. The script defines a `DatabaseHandler` class that sets up a connection to a SQLite database and provides methods for creating tables, inserting records, querying data, and closing the connection.

The third script, `finance_visualization.py`, is a financial data visualizer that uses Streamlit, Pandas, and Matplotlib. It defines a `DataVisualizer` class that takes in transaction data as a dictionary and converts it into a Pandas DataFrame. The class provides methods for displaying the data in a Streamlit dataframe and plotting line and bar charts of the transaction amounts over time.

Installation Instructions
-------------------------

To install the project, first clone the repository:

.. code-block:: bash

   git clone https://github.com/username/llm_github_actions.git

Next, navigate to the project directory and install the required dependencies using pip:

.. code-block:: bash

   cd llm_github_actions
   pip install -r requirements.txt

File Descriptions
-----------------

- `ocr_script.py`: A script that uses OCR to extract text from an image.
- `finance_script.py`: A script that manages financial transactions using SQLite.
- `finance_visualization.py`: A script that visualizes financial data using Streamlit, Pandas, and Matplotlib.
- `requirements.txt`: A list of required dependencies for the project.

Usage
-----

To use the OCR script, run `ocr_script.py` with the path to the Tesseract executable as an argument:

.. code-block:: bash

   python ocr_script.py /path/to/tesseract

To use the financial database manager, run `finance_script.py`:

.. code-block:: bash

   python finance_script.py

To use the financial data visualizer, run `finance_visualization.py`:

.. code-block:: bash

   python finance_visualization.py

Contributors
------------

- [Your Name]

License
-------

This project is licensed under the MIT License - see the `LICENSE` file for details.