import csv
import Scripts.myscript as script


def open_file():
    try:
        open_file.csv_file = open(
            'Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline="", encoding="utf-8")
        open_file.reader = csv.reader(open_file.csv_file, delimiter=';')
    except:
        FileExistsError


def get_data():
    data = []
    open_file()
    try:
        for row in open_file.reader:
            if row[2] != "Płeć":
                data.append(row)
    except:
        FileExistsError
    return data


data = get_data()


def test_average():
    assert script.average(2010, "Pomorskie", data) == 10481


def test_pass_rate_for_province():
    assert script.pass_rate_for_province("Pomorskie", data) == {
                                                                2010: 81, 2011: 78, 2012: 78, 2013: 79,
                                                                2014: 77, 2015: 77, 2016: 77, 2017: 77, 2018: 77
                                                                }


def test_province_compare():
    assert script.province_compare("Pomorskie", 'Lubuskie', data) == ((2018, 77), (2018, 79))


def test_best_province():
    assert script.best_province("2010", data) == ("Kujawsko-pomorskie", 82.87277995385523)


def test_regression_detection():
    assert script.regression_detection(data) == ("Dolnośląskie", 2011)

