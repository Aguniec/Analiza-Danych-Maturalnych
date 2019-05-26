import csv, sqlite3
import pandas

connection = sqlite3.connect("database.sql")
#connection.execute("CREATE TABLE t (Terytorium, Przystąpiłozdało, Płeć, Rok, Liczba osób);")
chunks = pandas.read_csv('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv',  chunksize=1000000, sep = ";")
for chunk in chunks:
    chunk.to_sql(name = "t", dtype = "text", con = connection, if_exists='append')
    print(chunk)

connection.execute("SELECT * FROM t").fetchall()

"""
connection = sqlite3.connect("database.sql")

connection.execute("CREATE TABLE t (Terytorium, Przystąpiłozdało, Płeć, Rok, Liczba osób);")

with open ('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv',  'r') as f:
    reader = csv.reader(f, delimiter = ";")
    data = next(reader)
    query = 'insert into t values ({})'
    query = query.format(','.join('?' * len(data)))
    cursor = connection.cursor()
    cursor.execute(query, data)
    for data in reader:
        cursor.execute(query, data)


    cursor.execute("SELECT * FROM t")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.commit()

"""


