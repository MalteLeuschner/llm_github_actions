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

.. OCR- und Finanzdatenvisualisierungsprojekt ..

****************************************
* Projekttitel: OCR- und Finanzdatenvisualisierung *
****************************************

Dieses Projekt kombiniert optische Zeichenerkennung (OCR) mit Finanzdatenvisualisierung, um eine umfassende Lösung für die Verarbeitung und Visualisierung von Finanztransaktionen bereitzustellen. Es besteht aus drei Hauptkomponenten:

1. OCRHandler: Ein Handler, der Bilder mithilfe von Tesseract OCR verarbeitet und Text extrahiert.
2. DatabaseHandler: Ein Datenbankhandler, der eine SQLite-Datenbank verwendet, um Transaktionen zu speichern und zu verwalten.
3. DataVisualizer: Ein Klasse zur Visualisierung von Finanzdaten mit Streamlit und Matplotlib.

**************************
* Projektbeschreibung *
**************************

Das Hauptziel dieses Projekts ist die Automatisierung der Textextraktion aus Bildern von Finanztransaktionen und deren Speicherung in einer Datenbank. Anschließend werden die Daten visualisiert, um Einblicke in die Finanzen zu gewinnen.

****************************************
* Installationsanweisungen *
****************************************

Um dieses Projekt zu installieren, müssen Sie die folgenden Abhängigkeiten installieren:

* Tesseract OCR (https://github.com/tesseract-ocr/tesseract)
* Pillow (https://pillow.readthedocs.io/en/stable/)
* Pandas (https://pandas.pydata.org/)
* Streamlit (https://streamlit.io/)
* Matplotlib (https://matplotlib.org/)

Führen Sie den folgenden Befehl aus, um die Anforderungen zu installieren:

.. code-block:: bash

   pip install -r requirements.txt

****************************************
* Verzeichnisstruktur *
****************************************

.. code-block:: bash

   .
   ├── ocr_handler.py
   ├── database_handler.py
   ├── data_visualizer.py
   ├── main.py
   └── requirements.txt

****************************************
* Dateibeschreibungen *
****************************************

* ocr\_handler.py:

  - OCRHandler Class:
    - Initialisierungsmethode (__init__)
    - perform\_ocr Methode

* database\_handler.py:

  - DatabaseHandler Class:
    - `__init__` Methode
    - create\_table Methode
    - insert\_transaction Methode
    - query\_transactions Methode
    - close Methode

* data\_visualizer.py:

  - DataVisualizer Class:
    - `__init__` Methode
    - display\_data Methode
    - plot\_line\_chart Methode
    - plot\_bar\_chart Methode

* main.py:
  - main Funktion

****************************************
* Nutzung *
****************************************

1. Verwenden Sie den OCRHandler, um Text aus Bildern von Finanztransaktionen zu extrahieren.
2. Verwenden Sie den DatabaseHandler, um die extrahierten Daten in einer SQLite-Datenbank zu speichern.
3. Verwenden Sie den DataVisualizer, um die Daten visuell darzustellen und Einblicke zu gewinnen.

****************************************
* Beitragende *
****************************************

- [Ihr Name]

****************************************
* Lizenz *
****************************************

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei LICENSE.

****************************************
* Programmablauf *
****************************************

1. Die main-Funktion wird aufgerufen, wenn das Skript ausgeführt wird.
2. Ein OCRHandler-Objekt wird mit dem Pfad zum Tesseract-Befehl initialisiert.
3. Die perform\_ocr-Methode wird auf dem OCRHandler-Objekt aufgerufen, wobei der Pfad zur Bilddatei als Argument übergeben wird.
4. Das Bild wird geöffnet und der Text innerhalb der Bilddatei wird mithilfe von Tesseract OCR extrahiert.
5. Das extrahierte Text wird ausgegeben.
6. Ein DatabaseHandler-Objekt wird initialisiert.
7. Eine Transaktion wird in die Datenbank eingefügt.
8. Alle Transaktionen werden aus der Datenbank abgefragt und ausgegeben.
9. Das DatabaseHandler-Objekt wird geschlossen.
10. Ein DataVisualizer-Objekt wird mit den Finanztransaktionen initialisiert.
11. Die Finanztransaktionen werden mithilfe von Streamlit in einem Tabellenformat ausgegeben.
12. Ein Liniendiagramm wird mithilfe von Matplotlib und Streamlit erstellt und angezeigt.
13. Ein Balkendiagramm wird mithilfe von Matplotlib und Streamlit erstellt und angezeigt.