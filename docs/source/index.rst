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


=====================
LLM GitHub Actions
=====================

Project Description
-------------------

The LLM GitHub Actions project is a simple Optical Character Recognition (OCR) tool that utilizes the pytesseract library to extract text from an image. The main component of the program is the `OCRHandler` class, which initializes an OCRHandler instance and sets up the tesseract command for the OCR process. The `perform_ocr` method of the OCRHandler class takes an image path as an argument, opens the image, reads the text in it using Tesseract OCR, and returns the extracted text.

The project also includes a Python application that uses SQLite to manage financial transactions. The main components of this script are the `DatabaseHandler` class and the `main` function. The `DatabaseHandler` class is responsible for handling database operations, such as creating a connection to a SQLite database, creating a table for transactions if it doesn't exist, and providing methods to insert transactions and query existing ones.

Additionally, the project contains a script that consists of a main function and a `DataVisualizer` class. The `DataVisualizer` class is designed to visualize financial data using Streamlit for the user interface, Pandas for data manipulation, and Matplotlib for data visualization.

Installation Instructions
-------------------------

To install the project, first clone the repository:

.. code-block:: bash

   git clone https://github.com/username/llm_github_actions.git

Next, navigate to the project directory:

.. code-block:: bash

   cd llm_github_actions

Create a virtual environment and activate it:

.. code-block:: bash

   python3 -m venv venv
   source venv/bin/activate

Install the required dependencies:

.. code-block:: bash

   pip install -r requirements.txt

File Descriptions
------------------

- `ocr.py`: Contains the `OCRHandler` class for performing OCR on images using the Tesseract OCR engine.
- `finance_manager.py`: Contains the `DatabaseHandler` class for managing financial transactions using SQLite.
- `finance_visualizer.py`: Contains the `DataVisualizer` class for visualizing financial data using Streamlit, Pandas, and Matplotlib.

Usage
-----

To use the OCR functionality, run the `ocr.py` script:

.. code-block:: bash

   python ocr.py

To use the financial manager, run the `finance_manager.py` script:

.. code-block:: bash

   python finance_manager.py

To use the data visualizer, run the `finance_visualizer.py` script:

.. code-block:: bash

   python finance_visualizer.py

Contributors
------------

- [Your Name]

License
-------

This project is licensed under the MIT License - see the `LICENSE` file for details.