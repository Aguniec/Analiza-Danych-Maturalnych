import csv
import math
import operator



def open_file():
    open_file.csv_file = open(
        'Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline="", encoding="utf-8")
    open_file.reader = csv.reader(open_file.csv_file, delimiter=';')


def menu():
#    os.system('cls' if os.name == 'nt' else 'clear')
    print("Super program!")
    print("Instrukcje:")
    print("Wpisz 1, aby obliczyć średnią lilość osób przystępujących do matury w danym województwie")
    print("Wpisz 2, aby obliczyć procentowej zdawalności dla danego województwa na przestrzeni lat")
    print("Wpisz 3, aby znależć województwo o najlepszej zdawalności w danym roku")
    print("Wpisz 4, aby wykryć województwa, które zanotowały regresję")
    print('Wpisz 5, aby porównać zdawlaność w dwóch województwach')
    print("Wpisz 6, aby wrócić do tego ekranu")
    print("Wpisz esc aby wyjść")
    check_input()


def check_input():
    while input != "esc":
        print("Wpisz polecenie:")
        command = input()
        if command == "1":
            average(year="")
        elif command == "2":
            pass_rate_for_voivodeship(voivodeship="")
        elif command == "3":
            best_voivodeship(year="")
        elif command == "4":
            regression_detect(year="")
        elif command == "5":
            voivodeship_compare(voivodeship_1 = "", voivodeship_2 = "")
        elif command == "6":
            menu()
        elif command == "esc":
            raise SystemExit
        else:
            print("Nieznane polecenie")
    return command

def program():
    menu()


def set_of_all_voivodeship():
    open_file()
    open_file.csv_file.readline()
    vio_set = set()        
    for row in open_file.reader:
        vio_set.add(row[0])
    return vio_set  


def set_of_all_years():
    open_file()
    open_file.csv_file.readline()
    year_set_temp = []
    for row in open_file.reader:
        year_set_temp.append(int(row[3]))
    year_set = []
    for new_element in year_set_temp:
        if not new_element in year_set:
            year_set.append(new_element)

    return year_set


def average(year, voivodeship):
    year = int(input("Type year: "))
    voivodeship = input("Type viovodoship: ")
    open_file()
    array_of_people = []
    try: 
        for row in open_file.reader:
            for i in range(2010, year+1):
                if (row[0] == voivodeship and row[1] == "przystąpiło") and row[3] == str(i):
                    array_of_people.append(int(row[4]))
        sum_of_people = sum(array_of_people)
        average_quantity_of_people = math.floor(sum_of_people / len (array_of_people))
        print (average_quantity_of_people)
    except:
        print("Invalid year or viovodeship")
    return average_quantity_of_people


def percentage_dict_for_voivodeship(voivodeship):
    proceed_to_the_exam = []
    pass_the_exam = []
    percentage_rate_dict= {}
    year_set = set_of_all_years()
    open_file()
    try:
        for year in range(min(year_set), max(year_set)+1):
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
    except:
        print("Incorrect viovodoship")
    return percentage_rate_dict


def pass_rate_for_voivodeship(voivodeship):
    voivodeship = input("Type viovodoship: ")
    pass_items = percentage_dict_for_voivodeship(voivodeship)
    for i in (pass_items):
        print(i, "-", pass_items[i], "%")


def voivodeship_compare(voivodeship_1, voivodeship_2):
    voivodeship_1 = input("Type first voivodeship : ")
    voivodeship_2 = input("Type second voivodeship: ")
    voivodeship_compare_1 = percentage_dict_for_voivodeship(voivodeship_1)
    voivodeship_compare_2 = percentage_dict_for_voivodeship(voivodeship_2)
    for x_value, y_value in zip(voivodeship_compare_1.items(), voivodeship_compare_2.items()):
        if x_value > y_value:
            print(x_value[0], voivodeship_1)
        elif x_value < y_value:
            print(x_value[0], voivodeship_2)
        else:
            print(x_value[0], "Equal")


def best_voivodeship(year):
    year = input("Podaj rok: ")
    pass_rate_dict = pass_rate_dict_maker(year)
    max_pass_value = max(list(pass_rate_dict.values()))

    print(max(pass_rate_dict.items(), key=operator.itemgetter(1)))
    print(max(pass_rate_dict.items(), key=operator.itemgetter(1))[0], "-", math.floor(max_pass_value), "%")


def pass_rate_dict_maker(year):
    open_file()
    proceed_women_dict = {}
    proceed_man_dict = {}
    pass_women_dict = {}
    pass_man_dict = {}
    for row in open_file.reader:
        if row[3] == year and row[0] != "Polska":
            if row[1] == "przystąpiło" and row[2] == "mężczyźni":
                proceed_man_dict[row[0]] = int(row[4])
            elif row[1] == "przystąpiło" and row[2] == "kobiety":
                proceed_women_dict[row[0]] = int(row[4])
            elif row[1] == "zdało" and row[2] == "mężczyźni":
                pass_man_dict[row[0]] = int(row[4])
            else:
                pass_women_dict[row[0]] = int(row[4])

    proceed_dict = {k: (proceed_man_dict[k]+proceed_women_dict[k]) for k in proceed_women_dict}
    pass_dict = {k: (pass_man_dict[k]+pass_women_dict[k]) for k in pass_women_dict}
    pass_rate_dict = {k: (float(pass_dict[k]/proceed_dict[k]*100)) for k in proceed_dict}

    return pass_rate_dict


def rate_calculator():
    year_set = set_of_all_years()
    open_file()
    proceed_women_dict = {}
    proceed_man_dict = {}
    pass_women_dict = {}
    pass_man_dict = {}
    all_items_list = []
    for year in year_set:
        open_file.csv_file.seek(0)
        for row in open_file.reader:
            if row[3] == str(year) and row[0] != "Polska":
                if row[1] == "przystąpiło" and row[2] == "mężczyźni":
                    proceed_man_dict[row[0]] = int(row[4])
                elif row[1] == "przystąpiło" and row[2] == "kobiety":
                    proceed_women_dict[row[0]] = int(row[4])
                elif row[1] == "zdało" and row[2] == "mężczyźni":
                    pass_man_dict[row[0]] = int(row[4])
                else:                
                    pass_women_dict[row[0]] = int(row[4]) 
        proceed_dict = {k: (proceed_man_dict[k]+proceed_women_dict[k]) for k in proceed_women_dict}
        pass_dict = {k: (pass_man_dict[k]+pass_women_dict[k]) for k in pass_women_dict}
        pass_rate_dict = {k: float(pass_dict[k]/proceed_dict[k]*100) for k in proceed_dict}
        for k,v in pass_rate_dict.items():
            all_items_list.append([k, year, v])

    return all_items_list


def temporary():

    all_items_list = rate_calculator()
    all_items_list.sort()
    for i in range(len(all_items_list)):
        if (all_items_list[i][0] == all_items_list[i-1][0]) and (all_items_list[i][2] < all_items_list[i-1][2]):
                print(all_items_list[i][0], all_items_list[i][1], "Regresja")

def test():
    year_set = set_of_all_years()
    proceed_women_dict = {}
    proceed_man_dict = {}
    pass_women_dict = {}
    pass_man_dict = {}
    all_items_list = []
    for year in range(len(year_set)):
        pass_rate_dict = pass_rate_dict_maker(year)
        print(pass_rate_dict)

#    print(all_items_list)


if __name__ == "__main__":
#    test()
#    average(year="", voivodeship="")
#    pass_rate_for_voivodeship(voivodeship="")
    best_voivodeship(year="")

