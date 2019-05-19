

import csv
import os
import math
#Suma i średnia wszystkich zdających dla danego województwa i roku

with open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline="", encoding="utf-8") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=';')

    def avearge():
        total = []
        for row in csvreader:
            if row[3] == "2010" and row[0] == "Lubuskie":
                total_array = total.append(row[4])

        total_sum = sum([int(i) for i in total])
        total_avg = int(total_sum / len(total))

        print("Total avearge: ", total_avg)

    avearge()

#Stosunek zdanych egzaminów

    def pass_rate():
        
        proceed_to_the_exam = []
        pass_the_exam = []
        dict_of_rate = {}
        for year in range(2010, 2019):  
            csv_file.seek(0)
            for row in csvreader:
                if row[1] == "przystąpiło" and row[0] == "Lubuskie":
                    if int(row[3]) == year:                        
                        proceed_to_the_exam.append(row[4])   
                if row[1] == "zdało" and row[0] == "Lubuskie":
                    if int(row[3]) == year:
                        pass_the_exam.append(row[4])
            proceed_sum = sum([int(i) for i in proceed_to_the_exam])
            pass_sum = sum([int(i) for i in pass_the_exam])
            percentage_rate = math.floor(100 * (pass_sum / proceed_sum))
            dict_of_rate.__setitem__(year, percentage_rate)
            print(year,"-", percentage_rate, "%")
        print(dict_of_rate)

    pass_rate()



"""
import requests
import json

res = requests.get("https://api.dane.gov.pl/resources/17201")
res.json()
"""
