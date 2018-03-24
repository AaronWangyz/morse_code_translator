#######################################################################
#                                                                     #
# This file first creates a dictionary contains "A-Z" and "0-9", and  #
# assigns 0 as their value.                                           #
#                                                                     #
# Then take the return result from functions in Task2.py and Task3.py,#
# then take user input until it's valid or its an empty string.       #
#                                                                     #
# Then analyze the occurrence of each character (both "A-Z" and "0-9")#
# and print the result of analysis in the format of:                  #
#       Character: X                                                  #
#       Occurrence: #                                                 #
#                                                                     #
#######################################################################
#                                                                     #
# The program was implemented in python 3.6.4, under PyCharm Edu IDE. #
#                                                                     #
#######################################################################
#                                                                     #
#                               Usage                                 #
# The structure of the morse code dictionary will be displayed first, #
# then it's pretty similar with the first steps of Task2.py and       #
# Task3.py, that user is asked to keep entering until an empty input  #
# is received.                                                        #
#                                                                     #
# However, regular expression is introduced in this stage to limit    #
# the user action. The allowed inputs from user are limited in 1, 0   #
# and *, plus user has to follow the pattern of                       #
#               "digit(s)*digit(s)*digit(s)......(*)"                 #
# which means one and only one asterisk is allowed as delimiter.      #
#                                                                     #
# When the sign of end of input is found (a.k.a. empty input), a      #
# report will be generated showing the occurrence of the characters   #
# that were entered by the user.                                      #
#                                                                     #
#######################################################################
#                                                                     #
# Author: Yezhen Wang                                                 #
# Student ID: 2861 9943                                               #
# Email: ywan0072@student.monash.edu                                  #
# Date Created: March 21, 2018                                        #
# Last Modified: March 23, 2018, 01:47 PM                             #
#                                                                     #
#######################################################################

# import the previous built python files Task1.py, Task2.py and Task3.py
import Task1
import Task2
import Task3
import re

# create a dictionary contains each character as the "key"
# and a number of occurrence as its "value"
occ_dict = {
    # 26 English letters
    "A": 0, "B": 0, "C": 0,
    "D": 0, "E": 0, "F": 0,
    "G": 0, "H": 0, "I": 0,
    "J": 0, "K": 0, "L": 0,
    "M": 0, "N": 0, "O": 0,
    "P": 0, "Q": 0, "R": 0,
    "S": 0, "T": 0, "U": 0,
    "V": 0, "W": 0, "X": 0,
    "Y": 0, "Z": 0,
    # 10 numbers
    "0": 0, "1": 0, "2": 0,
    "3": 0, "4": 0, "5": 0,
    "6": 0, "7": 0, "8": 0,
    "9": 0
}

Task1.print_structure()

# combine the functions imported for Task2.py and Task3.py together,
# keep taking and processing the user input until the input is an empty string
while True:
    # assign the return value of Task2.take_input (should just be an input from user)
    # to "user_input" variable for later use
    user_input = Task2.take_input()

    # check if user input is empty string,
    # stop the loop if it is
    if user_input == "":
        break

    # if user input is not empty string,
    # start analyze the occurrence of each character
    else:
        # declare a variable that stores a regexp statement will be used to limit user action
        # regexp work as: one or many 0 or 1s, followed by zero or one asterisk. The pattern appears at least once.
        valid_input = "^([01]+\*?)+$"

        # check if the user input matches the regexp
        # if input is valid, keep execute the rest of the script
        if re.match(valid_input, user_input):
            print("\nYou entered: ", user_input, "\n")

        # if input is empty, stop the loop
        elif user_input == "":
            break

        # if input is invalid, prompt message ask user to re-enter until valid input is obtained
        else:
            while True:
                user_input = input("Invalid input! Please re-enter: \n")
                if re.match(valid_input, user_input):
                    print("\nYou entered: ", user_input, "\n")
                    break
                elif user_input == "":
                    break

        # pass "user_input" to Task3.process_input,
        # assign the return value of Task3.process_input (should be a list contains valid translations)
        # to "valid_list" variable for later use
        valid_list = Task3.process_input(user_input)

        # check if the return value of Task3.process_input is a single "?"
        # (a single "?" stands for all morse code entered were not translatable)
        if valid_list != ["?"]:

            # loop through the "valid_list", once detect a match with the key in "occ_dict",
            # increment the corresponding value for 1
            for valid_element in valid_list:
                if valid_element in occ_dict:
                    occ_dict[valid_element] += 1

        # print message if all morse code entered were not translatable
        else:
            print("No valid morse code!\n")


# loop through the "occ_dict" and print its elements properly
for keys, values in occ_dict.items():
    if values != 0:
        print("Character ", keys, " appeared ", values, "times.\n")
