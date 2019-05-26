#from Scripts import myscript
#from Scripts import myscript_newversion
import csv
import math




csv_file = open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline="", encoding="utf-8")
csv_file.reader = csv.reader(csv_file, delimiter=';')

data = csv_file.reader
year_set = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]


def average(year, province):

    array_of_people = []
    for row in data:
        for i in range(min(year_set), year + 1):
            if (row[0] == province and row[1] == "przystąpiło") and row[3] == str(i):
                array_of_people.append(int(row[4]))
    sum_of_people = sum(array_of_people)
    average_quantity_of_people = math.floor(
        sum_of_people / len(array_of_people))
    print(average_quantity_of_people)

    return average_quantity_of_people


def test_average():
    assert average(2010, "Pomorskie") == 10481


def percentage_dict_for_province(province):
    proceed_to_the_exam = []
    pass_the_exam = []
    percentage_rate_dict = {}
    for year in range(min(year_set), max(year_set)+1):
        for row in data:
            if row[0] == province and int(row[3]) == year:
                if row[1] == "przystąpiło":
                    proceed_to_the_exam.append(int(row[4]))
                if row[1] == "zdało":
                    pass_the_exam.append(int(row[4]))
        proceed_sum = sum(proceed_to_the_exam)
        pass_sum = sum(pass_the_exam)
        percentage_rate = math.floor(100 * (pass_sum / proceed_sum))
        percentage_rate_dict[year] = percentage_rate

    return percentage_rate_dict


def test_percentage_dict_for_province():
    assert percentage_dict_for_province("Pomorskie") == {}