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

.. image:: logo.png

OCR- und Finanzdatenvisualisierungsprojekt
=========================================

Dieses Projekt umfasst drei Hauptkomponenten:

1. OCRHandler: Eine Klasse, die Optical Character Recognition (OCR) auf Bildern mit dem Tesseract-OCR-Motor durchführt.
2. DatabaseHandler: Eine Klasse, die Datenbankoperationen mit SQLite durchführt und eine Tabelle für Transaktionen verwaltet.
3. DataVisualizer: Eine Klasse, die Finanzdaten visualisiert, indem sie Daten in Tabellen formatiert und Diagramme mit matplotlib und streamlit erstellt.

Projektinstallation
-------------------

Installieren Sie das Projekt mit den folgenden Schritten:

1. Clonen Sie das Repository:

   .. code:: bash

      git clone https://github.com/username/ocr-finance-project.git

2. Navigieren Sie in das Projektverzeichnis:

   .. code:: bash

      cd ocr-finance-project

3. Installieren Sie die Anforderungen:

   .. code:: bash

      pip install -r requirements.txt

Verzeichnisstruktur
-------------------

Die Verzeichnisstruktur des Projekts ist wie folgt:

* ocr\_handler.py: Die OCRHandler-Klasse
* database\_handler.py: Die DatabaseHandler-Klasse
* data\_visualizer.py: Die DataVisualizer-Klasse
* main.py: Das Hauptskript, das die Klassen verwendet
* requirements.txt: Die Anforderungen für das Projekt

Dateibeschreibungen
-------------------

ocr\_handler.py
~~~~~~~~~~~~~~

* OCRHandler-Klasse
* Initialisierungsmethode mit Tesseract-Pfad
* OCR-Methode für Bilder

database\_handler.py
~~~~~~~~~~~~~~~~~~~~

* DatabaseHandler-Klasse
* Initialisierungsmethode mit Datenbankverbindung
* Methoden für Tabellenverwaltung, Transaktionsverwaltung und Datenabfrage

data\_visualizer.py
~~~~~~~~~~~~~~~~~~~

* DataVisualizer-Klasse
* Methoden für Datenanzeige in Tabellen und Diagrammen

Nutzung
--------

1. Führen Sie die OCR mit dem folgenden Befehl aus:

   .. code:: bash

      python ocr_handler.py path/to/image.png

2. Verwenden Sie die Datenbank mit den Methoden in database\_handler.py
3. Visualisieren Sie Daten mit dem folgenden Befehl:

   .. code:: bash

      python data_visualizer.py

Beitragende
----------

* Ihr Name
* Weitere Beitragende

Lizenz
-------

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei `LICENSE`.