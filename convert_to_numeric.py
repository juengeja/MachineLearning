import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('neue_datenbank_all.db')

# SQL-Abfrage ausführen und Ergebnis in ein Pandas-Dataframe laden
df_dropped = pd.read_sql("SELECT * FROM neue_tabelle_mit_allen_Daten", conn)

# Verbindung schließen
conn.close()

# Date mit integer-Werten austauschen
df_dropped['date_int'] = df_dropped['date'].apply(lambda x: int(x.replace('-', '').replace(' ', '').replace(':', '')))
df_dropped = df_dropped.drop('date', axis=1)
df_dropped = df_dropped.rename(columns={'date_int': 'date'})

# Vorgabe erstellen, wie Werte umgewandelt werden sollen
outcome_map = {'Win': 1, 'Lose': -1, 'Draw': 0}

# Ergebnislabel in integer-Werte umwandeln
df_dropped['label_outcome_int'] = df_dropped['label_outcome'].map(outcome_map)

# Ursprüngliche Spalte mit neuer Spalte ersätzen
df_dropped['label_outcome'] = df_dropped['label_outcome_int']

# temporäre Label-Daten löschen
df_dropped = df_dropped.drop('label_outcome_int', axis=1)

# Saison in das Anfangsjahr umwandeln und als integer-Spalte abspeichern
df_dropped['season'] = df_dropped['season'].str.split('/').str[0].astype(int)

# date und label_outcome als integer-Spalte abspeichern
df_dropped["date"] = df_dropped["date"].astype(int)
df_dropped["label_outcome"] = df_dropped["label_outcome"].astype(int)

print(df_dropped.dtypes)
