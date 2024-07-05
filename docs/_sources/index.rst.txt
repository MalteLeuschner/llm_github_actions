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
Projekt: OCR- und Finanzdatenvisualisierungs-Skript
=======================

Dieses Skript ist ein Python-Programm, das die pytesseract-Bibliothek verwendet, um Optical Character Recognition (OCR) auf einem Bild durchzuführen. Das Programm definiert eine Klasse ``OCRHandler`` und eine Funktion ``main()``.

Die Klasse ``OCRHandler`` wird verwendet, um OCR auf Bildern durchzuführen. Sie initialisiert eine Instanz der Klasse mit dem Pfad zum Tesseract-Befehlszeilentool. Der Tesseract-OCR-Engine wird verwendet, um Text aus Bildern zu extrahieren. Die Klasse verfügt über eine Methode, ``perform_ocr()``, die eine Bildpfad als Eingabe verwendet und den extrahierten Text als Zeichenfolge zurückgibt.

Die Funktion ``main()`` ist der Einstiegspunkt des Programms. Sie erstellt eine Instanz der ``OCRHandler``-Klasse mit dem Pfad zum Tesseract-Befehlszeilentool. Anschließend wird OCR an einer Bilddatei namens "balance\_sheet.png" mithilfe der ``perform_ocr()``-Methode der ``OCRHandler``-Instanz durchgeführt. Schließlich wird der extrahierte Text ausgegeben.

Das Programm verwendet die ``Image``-Klasse aus der PIL-Bibliothek, um die Bilddatei zu öffnen. Die Funktion ``pytesseract.image_to_string()`` wird verwendet, um Text aus dem Bild zu extrahieren.

Zusammenfassend bietet die ``OCRHandler``-Klasse eine bequeme Möglichkeit, OCR an Bildern mithilfe des Tesseract-OCR-Engines durchzuführen. Die Funktion ``main()`` zeigt, wie die ``OCRHandler``-Klasse verwendet wird, um Text aus einer Bilddatei zu extrahieren.

.. toctree::
   :maxdepth: 2
   ocr
   database
   dataviz

=======================
Verzeichnisstruktur
=======================

- ``ocr.py``: Enthält die Definition der ``OCRHandler``-Klasse und der ``main()``-Funktion.
- ``database.py``: Enthält die Definition der ``DatabaseHandler``-Klasse.
- ``dataviz.py``: Enthält die Definition der ``DataVisualizer``-Klasse und der ``main()``-Funktion.

=======================
ocr.py
=======================

.. automodule:: ocr
   :members:
   :undoc-members:
   :show-inheritance:

=======================
database.py
=======================

.. automodule:: database
   :members:
   :undoc-members:
   :show-inheritance:

=======================
dataviz.py
=======================

.. automodule:: dataviz
   :members:
   :undoc-members:
   :show-inheritance:

=======================
Installation
=======================

Um das Skript auszuführen, sind die folgenden Python-Bibliotheken erforderlich:

- pytesseract
- PIL
- pandas
- matplotlib
- streamlit

Installieren Sie diese Bibliotheken mithilfe von pip:

.. code-block:: bash

   pip install pytesseract pillow pandas matplotlib streamlit

Stellen Sie sicher, dass Tesseract auf Ihrem System installiert ist. Weitere Informationen zur Installation von Tesseract finden Sie unter https://github.com/tesseract-ocr/tesseract/wiki.

=======================
Nutzung
=======================

Führen Sie die ``main()``-Funktion in den Modulen ``ocr.py``, ``database.py`` und ``dataviz.py`` aus, um die Funktionalität des Skripts zu demonstrieren.

.. code-block:: bash

   python ocr.py
   python database.py
   python dataviz.py

=======================
Beitragende
=======================

- Ihr Name

=======================
Lizenz
=======================

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei ``LICENSE``.