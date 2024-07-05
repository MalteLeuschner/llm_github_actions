.. llm_github_actions documentation master file, created by
   sphinx-quickstart on Fri Jul  5 08:16:59 2024.
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
--------------------

The LLM GitHub Actions project is a collection of Python scripts that demonstrate the use of Optical Character Recognition (OCR) to extract text from images, a financial database manager using SQLite, and a financial data visualizer using Streamlit, Pandas, and Matplotlib.

The OCR script defines a single class `OCRHandler` that takes a Tesseract executable path as an argument and has a method `perform_ocr` to extract text from an image. The financial database manager script defines a `DatabaseHandler` class that sets up a connection to a SQLite database and provides methods to create, modify, and query the database. The financial data visualizer script defines a `DataVisualizer` class that takes transaction data as input and displays it in a Streamlit app with various charts.

Installation Instructions
-------------------------

To install the project, first clone the repository:

.. code-block:: bash

   git clone https://github.com/username/llm_github_actions.git

Next, navigate to the project directory:

.. code-block:: bash

   cd llm_github_actions

To install the required packages, create a virtual environment and activate it:

.. code-block:: bash

   python3 -m venv venv
   source venv/bin/activate

Then, install the required packages:

.. code-block:: bash

   pip install -r requirements.txt

File Descriptions
------------------

- `ocr.py`: A script that uses OCR to extract text from images.
- `financial_database_manager.py`: A script that manages financial transactions using SQLite.
- `financial_data_visualizer.py`: A script that visualizes financial data using Streamlit, Pandas, and Matplotlib.

Usage
-----

To use the OCR script, run the following command:

.. code-block:: bash

   python ocr.py path/to/image.png

To use the financial database manager script, run the following command:

.. code-block:: bash

   python financial_database_manager.py

To use the financial data visualizer script, run the following command:

.. code-block:: bash

   streamlit run financial_data_visualizer.py

Contributors
------------

- [Your Name]

License
-------

This project is licensed under the MIT License. See the `LICENSE` file for more information.