import csv
import math
import operator


def open_file():
    open_file.csv_file = open(
        'Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline="", encoding="utf-8")
    open_file.reader = csv.reader(open_file.csv_file, delimiter=';')


def average(year, voivodeship):
    year = input()
    voivodeship = input()
    total = []
    open_file()
    try:
        for row in open_file.reader:
            if row[3] == year and row[0] == voivodeship:
                for i in range(2010,int(year)+1):
                    total.append(int(row[4]))
        total_sum = sum(total)
        total_avg = int(total_sum / len(total))

        print("Total average: ", total_avg)
    except:
        print("Incorrect year or voivodeship")


class VoivodeshipDependency():

    def percentage_dict_for_voivodeship(voivodeship):
        proceed_to_the_exam = []
        pass_the_exam = []
        percentage_rate_dict= {}
        open_file()
        try:
            for year in range(2010, 2019):
                open_file.csv_file.seek(0)
                for row in open_file.reader:
                    if row[0] == voivodeship and int(row[3]) == year:
                        if row[1] == "przystąpiło":
                            proceed_to_the_exam.append(int(row[4]))
                        if row[1] == "zdało":
                            pass_the_exam.append(int(row[4]))
                proceed_sum = sum(proceed_to_the_exam)
                pass_sum = sum(pass_the_exam)
                percentage_rate = math.floor(100 * (pass_sum / proceed_sum))
                percentage_rate_dict[year] = percentage_rate
    #            print(year, "-", percentage_rate, "%")
        except:
            print("Incorrect voivodeship")

        return percentage_rate_dict

    def pass_rate_for_voivodeship(voivodeship):
        voivodeship = input()
        pass_items = VoivodeshipDependency.percentage_dict_for_voivodeship(voivodeship)
        for i in (pass_items):
            print(i, pass_items[i], "%")

    def voivodeship_compare(voivodeship_1, voivodeship_2):
        voivodeship_1 = input()
        voivodeship_2 = input()
        voivodeship_compare_1 = VoivodeshipDependency.percentage_dict_for_voivodeship(voivodeship_1)
        voivodeship_compare_2 = VoivodeshipDependency.percentage_dict_for_voivodeship(voivodeship_2)
        for x_value, y_value in zip(voivodeship_compare_1.items(), voivodeship_compare_2.items()):
            if x_value > y_value:
                print(x_value[0], voivodeship_1)
            elif x_value < y_value:
                print(x_value[0], voivodeship_2)
            else:
                print(x_value[0], "Equal")



class YearDependency():

    def pass_rate_dict_maker(year):
        open_file()
        proceed_women_dict = {}
        proceed_man_dict = {}
        pass_women_dict = {}
        pass_man_dict = {}
        for row in open_file.reader:
            if row[3] == str(year):
                if row[1] == "przystąpiło" and row[2] == "mężczyźni":
                    proceed_man_dict[row[0]] = int(row[4])
                if row[1] == "przystąpiło" and row[2] == "kobiety":
                    proceed_women_dict[row[0]] = int(row[4])
                if row[1] == "zdało" and row[2] == "mężczyźni":
                    pass_man_dict[row[0]] = int(row[4])
                if row[1] == "przystąpiło" and row[2] == "kobiety":
                    pass_women_dict[row[0]] = int(row[4]) 
        proceed_dict = {k: (proceed_man_dict[k]+proceed_women_dict[k]) for k in proceed_women_dict}
        pass_dict = {k: (pass_man_dict[k]+pass_women_dict[k]) for k in pass_women_dict}
        pass_rate_dict = {k: (float(pass_dict[k]/proceed_dict[k]*100)) for k in proceed_dict}

        return pass_rate_dict

    def best_voivodeship(year):
        year = int(input())
        pass_rate_dict = YearDependency.pass_rate_dict_maker(year)
        max_pass_value = max(list(pass_rate_dict.values()))
        print(max(pass_rate_dict.items(), key=operator.itemgetter(1))
            [0], "-", math.floor(max_pass_value), "%")

    def regression_detect(year):
        year = int(input())    
        regression_second_dict = YearDependency.pass_rate_dict_maker(year - 1)
        regression_first_dict = YearDependency.pass_rate_dict_maker(year)       
        for x_value, y_value in zip(regression_first_dict.items(), regression_second_dict.items()):
            if x_value > y_value:
                print(x_value[0])        




if __name__ == "__main__":

    YearDependency.best_voivodeship(year = "")
#   VoivodeshipDependency.pass_rate_for_voivodeship(voivodeship="")
#   VoivodeshipDependency.voivodeship_compare(voivodeship_1="", voivodeship_2="")
#   YearDependency.regression_detect(year="")
    
#    average(year= "", voivodeship="")

