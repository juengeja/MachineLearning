import sqlite3
import pandas as pd


cnx = sqlite3.connect('database.sqlite')

player_data = pd.read_sql("SELECT id, player_api_id, player_name, birthday, height, weight FROM Player", cnx)
match_data = pd.read_sql("SELECT id, country_id, league_id, season, stage, date, match_api_id, home_team_api_id, away_team_api_id, home_team_goal, away_team_goal, home_player_1, home_player_2, home_player_3, home_player_4, home_player_5, home_player_6, home_player_7, home_player_8, home_player_9, home_player_10, home_player_11, away_player_1, away_player_2, away_player_3, away_player_4, away_player_5, away_player_6, away_player_7, away_player_8, away_player_9, away_player_10, away_player_11, goal, shoton, shotoff, foulcommit, card, cross, corner, possession, B365H, B365D, B365A FROM Match", cnx)


# Alle Spielerspalten selektieren
player_cols = ['home_player_1', 'home_player_2', 'home_player_3', 'home_player_4', 'home_player_5', 'home_player_6', 'home_player_7', 'home_player_8', 'home_player_9', 'home_player_10', 'home_player_11', 'away_player_1', 'away_player_2', 'away_player_3', 'away_player_4', 'away_player_5', 'away_player_6', 'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10', 'away_player_11']
    
# Horizontal zusammenführen
combined_players = pd.concat([match_data[col] for col in player_cols])

# Duplikate entfernen
unique_players = combined_players.drop_duplicates()
print(unique_players[0])

# Überprüfen ob jeder Wert der Serie in der Spalte "player_api_id" von player_data ist
mask = unique_players.isin(player_data['player_api_id'])

# Wenn Spieler nicht gefunden wurde, dann soll der Wert mit dem Erkennungswert -1 gekennzeichnet werden
unique_players[~mask] = -1

# Nun wir nach den möglichen Vorkommnissen von -1 geprüft
indices = unique_players.index[unique_players == -1]

# Die Anzahl der Vorkommnisse eines Wertes werden gezählt
counts = unique_players.value_counts()

# Anzahl, wie oft -1 vorkommt, wird ausgegeben
print(counts[-1])
print(indices)