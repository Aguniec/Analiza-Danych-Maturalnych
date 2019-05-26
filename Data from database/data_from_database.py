import sqlite3
import pandas

connection = sqlite3.connect("database.sql")
chunks = pandas.read_csv('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv',  chunksize=1000000, sep = ";", encoding = "utf-8")
for chunk in chunks:
    chunk.to_sql(name = "t", dtype = "text", con = connection, if_exists='append')
    print(chunk)

connection.execute("SELECT * FROM t").fetchall()


