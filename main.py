import sqlite3
import pandas as pd
import numpy as np
import test


cnx = sqlite3.connect('database.sqlite')
dfm = pd.read_sql_query("SELECT * FROM Match", cnx)

print(np.where(pd.isnull(dfm)))
