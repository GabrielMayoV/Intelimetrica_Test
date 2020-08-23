# import pandas
# import sqlite3
# import os
#
# path_to_db = os.path.join(os.getcwd(), 'Melp','db.sqlite3')
#
# con = sqlite3.connect(path_to_db)
# df = pandas.read_csv('restaurantes.csv')
#
# df.to_sql('api_restaurant',con,if_exists='append',index=False)
#
#
# con.close()
# 
#
from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import os

df = pd.read_csv('restaurantes.csv')

"postgres+psycopg2://postgres:postgres@localhost:5432/melp"

alchemyEngine           = create_engine("postgres+psycopg2://postgres:postgres@localhost:5432/melp")
postgreSQLConnection    = alchemyEngine.connect()
df.to_sql('api_restaurant',postgreSQLConnection,if_exists='append',index=False)
postgreSQLConnection.close()
