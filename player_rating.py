import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

cnx = sqlite3.connect('database.sqlite')

# initialisieren der Dataframes, die nicht durch SQL-Abfragen erzeugt/befüllt werden
df_all_players_home = pd.DataFrame()
df_all_players_away = pd.DataFrame()
df_overall_home_ratings = pd.DataFrame()
df_overall_away_ratings = pd.DataFrame()


# Besorgen der SpielID, Anzahl der Heimtore und Auswärtstore
df_match_info = pd.read_sql('''Select
    Match.match_api_id AS SpielID,
    Match.home_team_goal AS Heimtore,
    Match.away_team_goal AS Auswärtstore
FROM Match
WHERE Match.home_team_api_id = 8634''', cnx)


# dynamische query für die Spielernamen und IDs der 11 Heim-Spieler einer bestimmten Mannschaft      
for i in range(1, 12):
    query = '''SELECT
        Match.home_player_''' + str(i) + ''' AS HomeSpieler''' + str(i) + ''',
        Player.player_name AS HomeSpielername''' + str(i) + '''
    FROM Match
    INNER JOIN Team ON Match.home_team_api_id == Team.team_api_id
    INNER JOIN Player ON Match.home_player_''' + str(i) + ''' == Player.player_api_id
    WHERE Match.home_team_api_id = 8634'''
    df_tmp = pd.read_sql(query, cnx)
    df_all_players_home = pd.concat([df_all_players_home, df_tmp], axis=1, join="outer")

df = pd.concat([df_match_info, df_all_players_home], axis=1, join="outer")
df = df.dropna()


# dynamische query für die Spielernamen und IDs der 11 Auswärts-Spieler     
for i in range(1, 12):
    query = '''SELECT
        Match.away_player_''' + str(i) + ''' AS AwaySpieler''' + str(i) + ''',
        Player.player_name AS AwaySpielername''' + str(i) + '''
    FROM Match
    INNER JOIN Team ON Match.home_team_api_id == Team.team_api_id
    INNER JOIN Player ON Match.away_player_''' + str(i) + ''' == Player.player_api_id
    WHERE Match.home_team_api_id = 8634'''
    df_tmp = pd.read_sql(query, cnx)
    df_all_players_away = pd.concat([df_all_players_away, df_tmp], axis=1, join="outer")

df = pd.concat([df, df_all_players_away], axis=1, join="outer")
df = df.dropna()

# Trennen der Home- und Away-Spieler IDs von den restlichen Daten des Dataframes mit allen abgefragten Daten
df_home_player_ids = df[['HomeSpieler1', 'HomeSpieler2', 'HomeSpieler3', 'HomeSpieler4', 'HomeSpieler5', 'HomeSpieler6', 'HomeSpieler7', 'HomeSpieler8', 'HomeSpieler9', 'HomeSpieler10', 'HomeSpieler11']]
df_away_player_ids = df[['AwaySpieler1', 'AwaySpieler2', 'AwaySpieler3', 'AwaySpieler4', 'AwaySpieler5', 'AwaySpieler6', 'AwaySpieler7', 'AwaySpieler8', 'AwaySpieler9', 'AwaySpieler10', 'AwaySpieler11']]


# gerade nur auslesen des ersten Heimspiels des FC Barcelona und das Besorgen der durchschnittlichen Overall Ratings der Spieler des FC Barcelona dieses Spiels
for i, row in df_home_player_ids.iterrows():
    while i < 1:
        y = 0
        for i in range(1, 12):
            query = '''SELECT
                        AVG(Player_Attributes.overall_rating) AS RatingGesamt,
                        Player_Attributes.player_api_id AS SpielerID
                    FROM Player_Attributes
                    WHERE Player_Attributes.player_api_id = ''' + str(int(row[y]))
            df_tmp = pd.read_sql(query, cnx)
            df_overall_home_ratings = pd.concat([df_overall_home_ratings, df_tmp])
            y = y + 1


# Besorgen der durchschnittlichen Overall Ratings der Spieler des ersten Auswärtsgegners des FC Barcelona
for i, row in df_away_player_ids.iterrows():
    while i < 1:
        y = 0
        for i in range(1, 12):
            query = '''SELECT
                        AVG(Player_Attributes.overall_rating) AS RatingGesamt,
                        Player_Attributes.player_api_id AS SpielerID
                    FROM Player_Attributes
                    WHERE Player_Attributes.player_api_id = ''' + str(int(row[y]))
            df_tmp = pd.read_sql(query, cnx)
            df_overall_away_ratings = pd.concat([df_overall_away_ratings, df_tmp])
            y = y + 1
