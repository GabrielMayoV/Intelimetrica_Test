import pandas
import sqlite3
import os

path_to_db = os.path.join(os.getcwd(), 'Melp','db.sqlite3')

con = sqlite3.connect(path_to_db)
df = pandas.read_csv('restaurantes.csv')

df.to_sql('api_restaurant',con,if_exists='append',index=False)


con.close()
