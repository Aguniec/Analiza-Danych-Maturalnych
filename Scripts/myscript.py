import csv
import math
import operator
import os


def open_file():
    """Open csv file"""
    try:
        open_file.csv_file = open(
            'Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline="", encoding="utf-8")
        open_file.reader = csv.reader(open_file.csv_file, delimiter=';')
    except FileExistsError:
        print("File doesn't exist")


def get_data():
    """Creates a set of data that depends on the selected filter"""
    data = []
    sex_filter = input(
        "Set filter: (w - data for women, m - data for men, type nothing to get all the data): ")
    open_file()
    try:
        if sex_filter == "":
            for row in open_file.reader:
                if row[2] != "Płeć":
                    data.append(row)
        elif sex_filter == "m":
            for row in open_file.reader:
                if row[2] == "mężczyźni":
                    data.append(row)
        elif sex_filter == "w":
            for row in open_file.reader:
                if row[2] == "kobiety":
                    data.append(row)
        else:
            print("Wrong filter")

    except FileExistsError:
        pass
    return data


def menu():
    """Print available instructions"""
    clear_screen()
    print("Instructions: \n"
          "Type 1 to calculate the average number of people who take the matura exam in the given province \n"
          "Type 2 to calculate the rate of success for a given province over the years \n"
          "Type 3 to find the province with the best pass rate in a given year \n"
          "Type 4 to detect province that have regressed \n"
          "Type 5 to compare the pass rate in two provinces \n"
          "Type 6 to go back to this screen \n"
          "Type esc to exit")


def clear_screen():
    """Clear user interface screen"""
    os.system("cls" if os.name == "nt" else "clear")


def check_input():
    """Allows the user to select a command"""
    while input != "esc":
        print("Type command:")
        command = input()
        if command == "1":
            menu()
            year = get_year()
            province = get_province()
            data = get_data()
            average(year, province, data)
        elif command == "2":
            menu()
            province = get_province()
            data = get_data()
            pass_rate_for_province(province, data)
        elif command == "3":
            menu()
            year = get_year()
            data = get_data()
            best_province(year, data)
        elif command == "4":
            menu()
            regression_detection(data)
        elif command == "5":
            menu()
            province_1 = get_province()
            province_2 = get_province()
            data = get_data()
            province_compare(province_1, province_2, data)
        elif command == "6":
            menu()
        elif command == "esc":
            raise SystemExit
        else:
            print("Invalid command")
            check_input()

    return command


def get_year():

    year = int(input("Type year: "))
    return year


def get_province():

    province = input("Type province: ")
    return province


def program():

    try:
        menu()
        check_input()
    except:
        pass


def set_of_all_years(data):
    """Creates a set of available years"""
    year_set_temp = []
    try:
        for row in data:
            year_set_temp.append(int(row[3]))
        year_set = []
        for new_element in year_set_temp:
            if not new_element in year_set:
                year_set.append(new_element)

    except:
        print("Invalid data")
        pass
    return year_set


def percentage_dict_for_province(province, data):
    """Creates a dictionary with pass rate for selected province and all years"""
    proceed_to_the_exam = []
    pass_the_exam = []
    percentage_rate_dict = {}
    year_set = set_of_all_years(data)
    try:
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

    except:
        print("Incorrect province")
        pass

    return percentage_rate_dict

def pass_rate_dict_maker(year, data):
    """Creates a dictionary with pass rate for selected year"""
    proceed_women_dict = {}
    proceed_man_dict = {}
    pass_women_dict = {}
    pass_man_dict = {}

    try:
        for row in data:
            if row[3] == str(year) and row[0] != "Polska":
                if row[1] == "przystąpiło" and row[2] == "mężczyźni":
                    proceed_man_dict[row[0]] = int(row[4])
                elif row[1] == "przystąpiło" and row[2] == "kobiety":
                    proceed_women_dict[row[0]] = int(row[4])
                elif row[1] == "zdało" and row[2] == "mężczyźni":
                    pass_man_dict[row[0]] = int(row[4])
                else:
                    pass_women_dict[row[0]] = int(row[4])
        if bool(proceed_man_dict) == False:
            proceed_dict = proceed_women_dict
            pass_dict = pass_women_dict
        elif bool(proceed_women_dict) == False:
            proceed_dict = proceed_man_dict
            pass_dict = pass_man_dict
        else:
            proceed_dict = {
                k: (proceed_man_dict[k]+proceed_women_dict[k]) for k in proceed_women_dict
                }
            pass_dict = {
                k: (pass_man_dict[k]+pass_women_dict[k]) for k in pass_women_dict
                        }
        pass_rate_dict = {
            k: (float(pass_dict[k]/proceed_dict[k]*100)) for k in proceed_dict
            }
    except:
        pass

    return pass_rate_dict


def average(year, province, data):
    """Calculates the average number of people who take the matura exam in the given province and year"""
    year_set = set_of_all_years(data)
    array_of_people = []
    try:
        for row in data:
            for i in range(min(year_set), year+1):
                if (row[0] == province and row[1] == "przystąpiło") and row[3] == str(i):
                    array_of_people.append(int(row[4]))
        sum_of_people = sum(array_of_people)
        average_quantity_of_people = math.floor(
            sum_of_people / len(array_of_people))
        print(average_quantity_of_people)
    except:
        print("Invalid year or province")
        pass

    return average_quantity_of_people


def pass_rate_for_province(province, data):
    """Calculates the rate of success for a given province over the years"""

    pass_items = percentage_dict_for_province(province, data)
    try:
        for i in (pass_items):
            print(i, "-", pass_items[i], "%")
    except:
        print("Incorrect province")
        pass

    return pass_items


def province_compare(province_1, province_2, data):
    """Compares the pass rate in two provinces"""
    province_compare_1 = percentage_dict_for_province(province_1, data)
    province_compare_2 = percentage_dict_for_province(province_2, data)
    try:
        for x_value, y_value in zip(province_compare_1.items(), province_compare_2.items()):
            if x_value > y_value:
                print(x_value[0], province_1)
            elif x_value < y_value:
                print(x_value[0], province_2)
            else:
                print(x_value[0], "Provinces are equal")
    except:
        print("Incorrect province")
        pass

    return (x_value, y_value)


def best_province(year, data):
    """Finds the province with the best pass rate in a given year"""
    try:
        pass_rate_dict = pass_rate_dict_maker(year, data)
        max_pass_value = max(list(pass_rate_dict.values()))
        best_province_detected = max(pass_rate_dict.items(), key=operator.itemgetter(1))[0]
        print(best_province_detected, "-", math.floor(max_pass_value), "%")
    except:
        print("Incorrect year")
        pass

    return (best_province_detected, max_pass_value)


def regression_detection(data):
    """Detects province that have regressed"""
    all_items_list = []
    year_set = set_of_all_years(data)
    try:
        for year in year_set:
            pass_rate_dict = pass_rate_dict_maker(year, data)
            for key, value in pass_rate_dict.items():
                sublist = [key, year, value]
                all_items_list.append(sublist)
        all_items_list.sort()
        for i in range(len(all_items_list)):
            if (all_items_list[i][0] == all_items_list[i-1][0]) and \
                                                                (all_items_list[i][2] < all_items_list[i-1][2]):
                    print(all_items_list[i][0], ",", all_items_list[i][1], "- Regression detected")
    except:
        print("Invalid data set")
        pass

    return (all_items_list[1][0], all_items_list[1][1])


if __name__ == "__main__":

    program()
