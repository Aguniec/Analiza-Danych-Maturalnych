

import csv
import math
import operator

"""Suma i średnia wszystkich zdających dla danego województwa i roku """

#with open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline="", encoding="utf-8") as csv_file:
    
def avearge(csv_file, year, voivodeship):
    year = input()
    voivodeship = input()
    csvreader = csv.reader(csv_file, delimiter=';')
    total = []
    try:
        for row in csvreader:
            if row[3] == year and row[0] == voivodeship:
                total_array = total.append(row[4])

        total_sum = sum([int(i) for i in total])
        total_avg = int(total_sum / len(total))

        print("Total avearge: ", total_avg)
    except:
        print("Incorrect number or voivodeship")

#Stosunek zdanych egzaminów

def pass_rate(csv_file, voivodeship):
    voivodeship = input()
    csvreader = csv.reader(csv_file, delimiter=';')
    proceed_to_the_exam = []
    pass_the_exam = []
#    dict_of_rate = {}
    try : 
        for year in range(2010, 2019):  
            csv_file.seek(0)
            for row in csvreader:
                if row[1] == "przystąpiło" and row[0] == voivodeship:
                    if int(row[3]) == year:                        
                        proceed_to_the_exam.append(row[4])   
                if row[1] == "zdało" and row[0] == voivodeship:
                    if int(row[3]) == year:
                        pass_the_exam.append(row[4])
            proceed_sum = sum([int(i) for i in proceed_to_the_exam])
            pass_sum = sum([int(i) for i in pass_the_exam])
            percentage_rate = math.floor(100 * (pass_sum / proceed_sum))
    #        dict_of_rate.__setitem__(year, percentage_rate)
            print(year,"-", percentage_rate, "%")
    #    print(dict_of_rate)
    except:
        print("Incorrect voivodeship")


#Najlepsze województwo

def best_voivodeship(csv_file):
    csvreader = csv.reader(csv_file, delimiter=';')
    proceed_to_the_exam = []
    pass_the_exam = []
    dict_of_rate = {}
    for year in range(2010, 2019):  
        csv_file.seek(0)
        for row in csvreader:
            if row[1] == "przystąpiło" :
                if int(row[3]) == year:                        
                    proceed_to_the_exam.append(row[4])   
            if row[1] == "zdało" :
                if int(row[3]) == year:
                    pass_the_exam.append(row[4])
        
        proceed_sum = sum([int(i) for i in proceed_to_the_exam])
        pass_sum = sum([int(i) for i in pass_the_exam])
        percentage_rate = math.floor(100 * (pass_sum / proceed_sum))
        dict_of_rate.__setitem__(year, percentage_rate)
#            print(year,"-", percentage_rate, "%")
    list_of_values = list(dict_of_rate.values())
    print(list_of_values)

if __name__ == "__main__":
    with open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline="", encoding="utf-8") as csv_file:
#        avearge(csv_file, year = "", voivodeship = "")
        pass_rate(csv_file, voivodeship = "")
#        best_voivodeship(csv_file)
        

        

#    best_voivodeship()


"""
import requests
import json

res = requests.get("https://api.dane.gov.pl/resources/17201")
res.json()
"""
"""

def find_row_by_id(filename, key_column, id):
    with f = open(filename, 'rb'):
        my_reader = csv.reader(f)
        for row in my_reader:
            if row[key_column] == id:
                return row
    raise Error("Could not find row")

print find_by_row('eggs.csv', 2, my_id)
"""