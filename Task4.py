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
# Last Modified: March 28, 2018, 12:45 PM                             #
#                                                                     #
#######################################################################

# import the previous built python files Task1.py, Task2.py and Task3.py
import Task1
import Task2
import Task3
import re
from collections import Counter

# create a dictionary contains each character as the "key"
# and a number of occurrence as its "value"
occ_dict = {}
occ_total = {}

# declare a counter for loop control
count = 0

Task1.print_structure()

# combine the functions imported for Task2.py and Task3.py together,
# keep taking and processing the user input until the input is an empty string
while True:

    # for the first loop (count = 0),
    # assign the return value of Task2.take_input (should just be an input from user)
    # to "user_input" variable for later use
    if count == 0:
        user_input = Task2.take_input()

    # for later loops (count > 0), break the loop if the user input is empty
    elif count > 0 and user_input == "":
        break

    # keep taking user input if its not empty
    else:
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
                if re.match(valid_input, user_input):
                    print("\nYou entered: ", user_input, "\n")
                    break
                elif user_input == "":
                    break
                else:
                    user_input = input("Invalid input! Please re-enter: \n")

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
                else:
                    occ_dict[valid_element] = 1

            # print the occurrence for this single loop
            for keys, values in occ_dict.items():
                if values != 0:
                    print("Character ", keys, " appeared ", values, "times.\n")

        # print message if all morse code entered were not translatable
        else:
            print("No valid morse code!\n")

        # utilize "Counter" class to summarize the occurrence
        dict_counter = Counter(occ_dict)
        total_counter = Counter(occ_total)
        occ_total = dict(dict_counter + total_counter)

        # data already moved to "occ_total" so clear the "occ_dict" for next loop
        occ_dict.clear()

        # increment the counter after each loop
        count += 1


# loop through the "occ_total" and print its elements properly
print("Final Occurrence Analysis: \n")
for keys, values in occ_total.items():
    if values != 0:
        print("Character ", keys, " appeared ", values, "times.\n")
