

import csv
import os
import math
#Suma i średnia wszystkich zdających dla danego województwa i roku

with open("Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv", newline = "", encoding = "utf-8") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=";")

    def avearge():
        total = []
        for row in csvreader:
            if row["Rok"] == "2010" and row["Terytorium"] == "Lubuskie":
                total_array = total.append(row["Liczba osób"])

        total_sum = sum([int(i) for i in total])
        total_avg = int(total_sum / len(total))

        print("Total avearge: ", total_avg)

#    avearge()

    def pass_rate():
        proceed_to_the_exam = []
        pass_the_exam = []
        dict = {}
        for row in csvreader:
            if row["Rok"] == "2010": 
                if row["Przystąpiło/zdało"] == "przystąpiło":
                    proceed_exam = proceed_to_the_exam.append(row["Liczba osób"])

                if row["Przystąpiło/zdało"] == "zdało":
                    pass_exam = pass_the_exam.append(row["Liczba osób"])

            proceed_sum = sum([int(i) for i in proceed_to_the_exam])
            pass_sum = sum([int(i) for i in pass_the_exam])

            percentage_rate = math.floor(100* (pass_sum / proceed_sum))
            dict["2010"] = (str(percentage_rate)+ "%")
        print (percentage_rate, "%")
        print (dict)

    pass_rate()




"""
import requests
import json

res = requests.get("https://api.dane.gov.pl/resources/17201")
res.json()
"""
