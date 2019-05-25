from Scripts import myscript
import csv

def open_file():
    open_file.csv_file = open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline="", encoding="utf-8")
    open_file.reader = csv.reader(open_file.csv_file, delimiter=';')

def get_data():
    data = []
    filter = input(
        "Set filter: (w - data for women, m - data for men, type nothing to get all the data): ")
    open_file()
    try:
        if filter == "":
            for row in open_file.reader:
                if row[2] != "Płeć":
                    data.append(row)
        elif filter == "m":
            for row in open_file.reader:
                if row[2] == "mężczyźni":
                    data.append(row)
        elif filter == "w":
            for row in open_file.reader:
                if row[2] == "kobiety":
                    data.append(row)
        else:
            print("Wrong filter")

    return data
