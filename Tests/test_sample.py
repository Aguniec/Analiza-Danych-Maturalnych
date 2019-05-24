from Scripts import myscript
import csv

def open_file():
    open_file.csv_file = open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline="", encoding="utf-8")
    open_file.reader = csv.reader(open_file.csv_file, delimiter=';')


    def test_set_of_all_years():

        assert myscript.set_of_all_years(data) == [2010]
