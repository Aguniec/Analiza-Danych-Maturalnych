
import csv
import os
import math
import operator


class GetData:

    def __init__(self, data):
        self.data = data

    def get_data(self, sex_filter):
        """Select data for the selecte filter"""
        data_list = []
        self.sex_filter = input("Set filter: (w - data for women, m - data for men, type nothing to get all the data): ")

        if sex_filter == "":
            for row in self.data:
                if row[2] != "Płeć": data_list.append(row)
        elif sex_filter == "m":
            for row in self.data:
                if row[2] == "mężczyźni": data_list.append(row)
        elif sex_filter == "w":
            for row in self.data:
                if row[2] == "kobiety": data_list.append(row)
        else:
            print("Wrong filter")


        return data_list


class UserInterface:


    def menu(self):
        user_interface.clear_screen()

        print("Instructions: \n"
              "Type 1 to calculate the average number of people who take the matura exam in the given province \n"
              "Type 2 to calculate the rate of success for a given province over the years \n"
              "Type 3 to find the province with the best pass rate in a given year \n"
              "Type 4 to detect province that have regressed \n"
              "Type 5 to compare the pass rate in two provinces \n"
              "Type 6 to go back to this screen \n"
              "Type esc to exit")

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def check_input(self):

        """Check command typed by user"""
        while input != "esc":
            print("Type command:")
            self.command = input()

            if self.command == "1":
                user_command.average(year="", province="")

            elif self.command == "2":
                user_command.pass_rate_for_province(province="")

            elif self.command == "3":
                user_command.best_province(year="")

            elif self.command == "4":
                user_command.regression_detection()

            elif self.command == "5":
                user_command.province_compare(province_1="", province_2="")

            elif self.command == "6":
                user_interface.menu()

            elif self.command == "esc":
                raise SystemExit
            else:
                print("Invalid command")
                pass

        return self.command

    def program(self):
        user_interface.menu()
        user_interface.check_input()



class DataAnalysis :

    def __init__(self):
        imported_data = GetData(reader)
        self.data = imported_data.get_data(sex_filter = "")

    def set_of_all_years(self):
        """Return set of all avalible years"""
        year_set_temp = []
        try:
            for row in self.data:
                year_set_temp.append(int(row[3]))
            year_set = []
            for new_element in year_set_temp:
                if not new_element in year_set:
                    year_set.append(new_element)
        except:
            print("Invalid data")
            pass
        return year_set


    def average(self, year, province):
        """Return average of people for given year and province"""
        self.year = int(input("Type year: "))
        self.province = input("Type province: ")
        try :
            year_set = user_command.set_of_all_years()
            array_of_people = []
            for row in self.data:
                for i in range(min(year_set), self.year + 1):
                    if (row[0] == self.province and row[1] == "przystąpiło") and row[3] == str(i):
                        array_of_people.append(int(row[4]))
            sum_of_people = sum(array_of_people)
            average_quantity_of_people = math.floor(sum_of_people / len(array_of_people))

            print(average_quantity_of_people)
        except :
            print("Invalid year or province")

        return average_quantity_of_people


    def percentage_dict_for_province(self, province):
        """Return dict with percentage rate for given province"""
        proceed_to_the_exam = []
        pass_the_exam = []
        percentage_rate_dict = {}
        year_set = user_command.set_of_all_years()
        self.province = province
        try:
            for year in range(min(year_set), max(year_set) + 1):
                for row in self.data:
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


    def pass_rate_for_province(self, province):
        self.province = input("Type province: ")
        pass_items = user_command.percentage_dict_for_province(self.province)
        try:
            for i in (pass_items):
                print(i, "-", pass_items[i], "%")
        except:
            print("Incorrect province")
            pass

        return pass_items

    def province_compare(self, province_1, province_2):
        """Print between """
        self.province_1 = input("Type first province : ")
        self.province_2 = input("Type second province: ")
        province_compare_1 = user_command.percentage_dict_for_province(self.province_1)
        province_compare_2 = user_command.percentage_dict_for_province(self.province_2)
        try:
            for x_value, y_value in zip(province_compare_1.items(), province_compare_2.items()):
                if x_value > y_value:
                    print(x_value[0], self.province_1)
                elif x_value < y_value:
                    print(x_value[0], self.province_2)
                else:
                    print(x_value[0], "Provinces are equal")
        except:
            print("Incorrect province")
            pass

        return province_compare_1, province_compare_2

    def pass_rate_dict_maker(self, year):
        proceed_women_dict = {}
        proceed_man_dict = {}
        pass_women_dict = {}
        pass_man_dict = {}

        try:
            for row in self.data:
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
                    k: (proceed_man_dict[k] + proceed_women_dict[k]) for k in proceed_women_dict
                }
                pass_dict = {
                    k: (pass_man_dict[k] + pass_women_dict[k]) for k in pass_women_dict
                }
            pass_rate_dict = {
                k: (float(pass_dict[k] / proceed_dict[k] * 100)) for k in proceed_dict
            }
        except:
            pass

        return pass_rate_dict

    def best_province(self, year):
        self.year = input("Type year: ")
        try:
            pass_rate_dict = user_command.pass_rate_dict_maker(self.year)
            max_pass_value = max(list(pass_rate_dict.values()))
            print(max(pass_rate_dict.items(), key=operator.itemgetter(1))[0], "-", math.floor(max_pass_value), "%")
        except:
            print("Incorrect year")
            pass
        return max_pass_value


    def regression_detection(self):
        all_items_list = []

        year_set = user_command.set_of_all_years()
        try:
            for year in year_set:
                pass_rate_dict = user_command.pass_rate_dict_maker(year)
                for key, value in pass_rate_dict.items():
                    sublist = [key, year, value]
                    all_items_list.append(sublist)
            all_items_list.sort()
            for i in range(len(all_items_list)):
                if (all_items_list[i][0] == all_items_list[i - 1][0]) and \
                        (all_items_list[i][2] < all_items_list[i - 1][2]):
                    print(all_items_list[i][0], ",", all_items_list[i][1], "- Regression detected")
        except:
            print("Invalid data set")
            pass


csv_file = open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline="", encoding="utf-8")
reader = csv.reader(csv_file, delimiter=';')

imported_data = GetData(reader)
user_interface = UserInterface()
user_command = DataAnalysis()

user_interface.program()


