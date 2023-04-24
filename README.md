# MachineLearning
Dieses Repository gehört zum Projekt _"Soccer Outcome Prediction"_ der Gruppe 2 des Kurses WWI20SEA im Modul Machine Learning. Die Gruppenmitglieder sind:
* Leon Engelhardt
* Maik Kebernik
* Jannis Jüngert

In diesem Repository ist der gesamte Code des Projekts enthalten. Geschrieben und getestet wurde der Code in den Python-Versionen **3.11.2** und **3.11.3**, er sollte in diesen Versionen also lauffähig sein. Im folgenden soll kurz der Aufbau dieses Repos beschrieben werden.

## Aufbau
Im Laufe des Projekts wurde wie folgt vorgegangen: Die Datei "overall.ipynb" diente als Haupt-Datei. Hier wurden verschiedene Code-Blöcke geschrieben und laufend überarbeitet, um das Projekt voranzutreiben. Gleichzeitig wurden weitere Dateien zum Testen, oder zum Auslagern von Code-Blöcken, die in der "overall.ipynb" nicht mehr benötigt wurden, angelegt. Hier sollen die einzelnen Dateien im Repository jeweils kurz beschrieben werden.

### convert_to_numeric.py
In dieser Datei findet sich ausgelagerter Code, der dazu dient, die Datenbasis in numerische Daten umzuwandeln. Er wurde dazu genutzt, die Datei **neue_datenbank_numeric.db** anzulegen, die nur numerische Daten enthält. Da die numerischen Daten bereits in der zusätzlichen Datei persistiert sind, wird dieser Code in "overall.ipynb" nicht länger benötigt.

### data_preparation.ipynb
In dieser Datei sind diverse Methoden vorhanden. Zweck des Codes ist es, die ursprünglichen Daten aus der Datenbank aufzubereiten und durch neue Features anzureichern. Da für diesen Code jede Zeile der Datenbank durchlaufen werden muss, entstehen dabei sehr hohe Ausführungszeiten. Folglich wurde das Ergebnis in den neu erstellten Datenbanken (**neue_datenbank.db, neue_datenbank_500.db, neue_datenbank_all.db, neue_datenbank_numeric.db**) persisitiert. So kann dieser Code ausgelagert werden.

### main.py
Diese Datei wurde bei Anlage des Projekts automatisch generiert und zunächst auch für die initiale Phase des Projekts verwendet. Für den weiteren Verlauf wurde dann jedoch zu "overall.ipynb" als Notebook gewechselt, um einzelne Codeblöcke separat ausführen zu können.

### neue_datenbank.db, neue_datenbank_500.db, neue_datenbank_all.db und neue_datenbank_numeric.db
Diese Dateien wurden angelegt, um die bereinigten Daten in verschiedenen Ausführungen zu persistieren. So kann man unabhängig und ohne lange Laufzeiten auf die bereinigten Daten zugreifen. **neue_datenbank.db** enthält 30 Zeilen der bereinigten Daten, um komplexe Aufgaben mit geringer Laufzeit testen zu können. **neue_datenbank_500.db** enthält 500 Datensätze und erfüllt den selben Zweck, hier kann jedoch bereits mit Ergebnissen gerechnet werden, die eine grobe Richtung der späteren Ergebnisse mit allen Daten zeigen. **neue_datenbank_all.db** enthält alle bereinigten Datensätze. **neue_datenbank_numeric.db** beinhaltet eine Tabelle mit 30 bereinigten Datensätzen, eine mit 500 und eine mit allen. Die Besonderheit, die hier vorliegt, ist: Alle Daten in diesen Tabellen sind zu numerischen Daten umgewandelt worden. So können auch Anwendungen, die numerische Daten erfordern, mit allen Features genutzt werden.

### overall.ipynb
Bei "overall.ipynb" handelt es sich um das Herzstück des Projekts. Hier werden Machine Learning Modelle trainiert und die Ergebnisse ausgewertet. Über den Button "run all" können alle Auswertungen ausgegeben werden, je nach PC-Leistung dauert das ca. eine Stunde. Die bevorzugt Python Version ist 3.11.3.

### player_rating.ipynb, player_rating.py, player_stats.ipynb und players_complete_check.py
Diese Dateien enthalten Code zur Datenbereinigung und -anreicherung mit weiteren Features, außerdem zur Datenanalyse der genutzten Datenbank. Die Code-Schnipsel wurden entweder ausgelagert, zum Testen geschrieben oder als mögliche Alternativlösung geschrieben worden. Daher werden sie für "overall.ipynb" nicht benötigt, der Vollständigkeit halber sind sie dennoch hier enthalten.

### .png & .dot Dateien
Alle Dateien, die auf .png oder .dot enden sind Grafiken, die in "overall.ipynb" generiert werden und zwischengespeichert werden müssen.

## Vorraussetzungen
Zum Ausführen der Code-Blöcke des Random Forest Algorithmus muss die Software `graphviz` installiert sein.

Graphviz findet man hier: https://www.graphviz.org/download/

Außerdem müssen die importierten Bibliotheken über pip o.Ä. installiert werden.
