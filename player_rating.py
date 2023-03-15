import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

cnx = sqlite3.connect('database.sqlite')

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum(x1-x2)**2)

def get_data(team_api_id):
    # get Match data (SpielID, Heimtore, Auswärtstore)
    df_match_data = pd.read_sql(
        '''Select
            Match.match_api_id AS SpielID,
            Match.home_team_goal AS Heimtore,
        Match.away_team_goal AS Auswärtstore
        FROM Match
        WHERE Match.home_team_api_id = ''' + str(team_api_id), cnx)
    
    df_label = _set_label(df_match_data)
    df_all_player_ids_home = _get_involved_home_players(team_api_id)
    df_all_player_ids_away = _get_involved_away_players(team_api_id)
    df = pd.concat([df_match_data, df_all_player_ids_home, df_all_player_ids_away], axis=1, join="outer")
    df = df.dropna()

    df_all_player_ids_home_2 = df[['home_player_1', 'home_player_2', 'home_player_3', 'home_player_4', 'home_player_5', 'home_player_6', 'home_player_7', 'home_player_8', 'home_player_9', 'home_player_10', 'home_player_11', ]]
    df_all_player_ids_away_2 = df[['away_player_1', 'away_player_2', 'away_player_3', 'away_player_4', 'away_player_5', 'away_player_6', 'away_player_7', 'away_player_8', 'away_player_9', 'away_player_10', 'away_player_11']]

    df_home_team = pd.DataFrame(columns=['OverallRatingHome'])
    df_away_team = pd.DataFrame(columns=['OverallRatingAway'])
    df_teams = pd.DataFrame()

    df_home_team = (_get_team_rating(df_all_player_ids_home_2))
    df_away_team = (_get_team_rating(df_all_player_ids_away_2))

    df_teams = pd.concat([df_home_team, df_away_team, df_label], axis=1, join="outer")

    df_teams = df_teams.dropna()
    print(df_teams)




# set label ob ein Spiel gewonnen/verloren/unentschieden ausgegangen ist
def _set_label(dataframe):
    home_goals = dataframe['Heimtore']
    away_goals = dataframe['Auswärtstore']
    df_label_outcome = pd.DataFrame(columns=['Label'])

    y = 0
    for i in home_goals:
        if i > away_goals[y]:
            df_label_outcome.loc[y, 'Label'] = 'Win'
        if i < away_goals[y]:
            df_label_outcome.loc[y, 'Label'] = 'Lose'
        if i == away_goals[y]:
            df_label_outcome.loc[y, 'Label'] = 'Draw'
        y = y + 1
    return df_label_outcome


# get Player data für ein Match aller Heimspieler 1 - 11
def _get_involved_home_players(team_api_id):
    df_all_players_home = pd.DataFrame()   
    for i in range(1, 12):
        query = '''SELECT
            Match.home_player_''' + str(i) + '''
        FROM Match
        INNER JOIN Team ON Match.home_team_api_id == Team.team_api_id
        WHERE Match.home_team_api_id = ''' + str(team_api_id)
        df_tmp = pd.read_sql(query, cnx)
        #print(_get_player_ratings(df_tmp))
        df_all_players_home = pd.concat([df_all_players_home, df_tmp], axis=1, join="outer")
    return df_all_players_home


# get Player data für ein Match aller Auswärtsspieler 1 - 11
def _get_involved_away_players(team_api_id):
    df_all_players_away = pd.DataFrame()   
    for i in range(1, 12):
        query = '''SELECT
            Match.away_player_''' + str(i) + '''
        FROM Match
        INNER JOIN Team ON Match.home_team_api_id == Team.team_api_id
        WHERE Match.home_team_api_id = ''' + str(team_api_id)
        df_tmp = pd.read_sql(query, cnx)
        df_all_players_away = pd.concat([df_all_players_away, df_tmp], axis=1, join="outer")
    return df_all_players_away


# get Mean Overall Rating einer Mannschaft
def _get_team_rating(dataframe):
    df_result = pd.DataFrame(['OverallRatingTeam'])
    index = 0
    while index < 10:
        home_player_x = 0 
        df_ratings_of_a_team = pd.DataFrame(['Ratings'])
        while home_player_x < 11:
            id = dataframe.iat[int(index), home_player_x]
            df_tmp = pd.DataFrame()
            df_tmp = _get_player_rating(int(id))
            df_ratings_of_a_team.loc[home_player_x] = df_tmp.loc[0][0]
            home_player_x = home_player_x + 1
        df_result.loc[index] = df_ratings_of_a_team.mean()
        index = index + 1
    return df_result


# get Mean Overall Rating eines Spielers
def _get_player_rating(id):
    query = '''SELECT
    AVG(Player_Attributes.overall_rating)
    FROM Player_Attributes
    WHERE Player_Attributes.player_api_id = ''' + str(int(id))
    df_tmp = pd.read_sql(query, cnx)
    return df_tmp


# split data for training and evaluation (80% --- 20%)

get_data(8634)