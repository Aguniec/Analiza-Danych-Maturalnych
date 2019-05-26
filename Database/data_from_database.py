import csv, sqlite3
import pandas


connection = sqlite3.connect("database.sql")

connection.execute("CREATE TABLE t (Terytorium, Przystąpiłozdało, Płeć, Rok, Liczba osób);")

with open ('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv',  'r') as f:
    reader = csv.reader(f, delimiter = ";")
    data = next(reader)
    query = 'insert into t values ({0})'
    query = query.format(','.join('?' * len(data)))
    cursor = connection.cursor()
    cursor.execute(query, data)
    for data in reader:
        cursor.execute(query, data)
    connection.commit()

cur = connection.cursor()
cur.execute("SELECT * FROM t")

rows = cur.fetchall()

for row in rows:
    print(row)







#cur = conn.cursor()  # The database will be saved in the location where your 'py' file is saved

#c.execute(query)
#conn.commit()

#file = pandas.read_csv('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', sep = ";", encoding="utf-8")
#file_sql = file.to_sql(name="test",  con=conn, index = False)

#c.execute(''' SELECT * FROM test ''')
#print(c.fetchall())
#print(file)


"""

cur = con.cursor()
cur.execute("CREATE TABLE t (Terytorium, Przystąpiłozdało, Płeć, Rok, Liczba osob);")

with open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline="") as csv_file:
    dr = csv.DictReader(csv_file, delimiter=';') # comma is default delimiter
    to_db = [(i['Terytorium'], i['Przyst�pi�o/zda�o '], i['P�e� '], i['Rok'], i['Liczba os�b']) for i in dr]

cur.executemany("INSERT INTO t (Terytorium, Przystąpiłozdało, Płeć, Rok, Liczba osób) VALUES (?, ?);", to_db)
con.commit()
con.close()
"""