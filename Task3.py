#######################################################################
#                                                                     #
# This file declares a function called "process_input" that takes a   #
# param called "user_input".                                          #
#                                                                     #
# It also takes "morse_dict" built in Task1.py by import function.    #
#                                                                     #
# Then split the "user_input" by "*" and translate the morse code     #
# entered by user to the corresponding message.                       #
#                                                                     #
# The invalid morse code entered will be translated as "?" and the    #
# invalid morse code will be printed out after the message.           #
#                                                                     #
# The list of valid translations, "valid_list" will be the return     #
# value of function "process_input"                                   #
#                                                                     #
#######################################################################
#                                                                     #
# The program was implemented in python 3.6.4, under PyCharm Edu IDE. #
#                                                                     #
#######################################################################
#                                                                     #
#                               Usage                                 #
# Just like Task2.py, the program will prompt for user input after it #
# is executed, and user can keep entering text until an empty input is#
# received.                                                           #
#                                                                     #
# Instead of only display what user entered, this program will also   #
# try to translate the morse code entered by user, display the        #
# translated message, and list the user inputs that were not          #
# translatable.                                                       #
#                                                                     #
# Valid but untranslatable inputs will be displayed as "?" in the     #
# translated message.                                                 #
#                                                                     #
#######################################################################
#                                                                     #
# Author: Yezhen Wang                                                 #
# Student ID: 2861 9943                                               #
# Email: ywan0072@student.monash.edu                                  #
# Date Created: March 21, 2018                                        #
# Last Modified: March 24, 2018, 03:15 PM                             #
#                                                                     #
#######################################################################

# import morse_dict and user_input from previous python files
from Task1 import morse_dict
import Task2
import re


# create the function that processes the parameter passed to it
def process_input(user_input):

    # if the user input is empty, directly stop the function and return empty string
    if user_input == "":
        return user_input

    # declare lists for storing valid and invalid user input
    valid_list = []
    invalid_list = []

    # split the "user_input" by "*" and store into "split_input"
    split_input = user_input.split("*")

    # loop through "split_input", compare the elements with "morse_dict"
    # valid input (elements that exist in "morse_dict") will be append to "valid_list"
    # invalid input (elements that do not exist in "morse_dict") will be append to "invalid_list"
    # "?" will also be append to "valid_list" if an "invalid_input" is found
    for split_element in split_input:
        if split_element in morse_dict:
            valid_list.append(morse_dict[split_element])
        else:
            # valid_list.append("?")
            if split_element not in invalid_list:
                invalid_list.append(split_element)

    # declare a counter to check the content of "valid_list"
    count = 0

    # check if all the elements in "valid_list" are "?"
    # ("?" stands for untranslatable morse code)
    for item in valid_list:
        if item == "?":
            count += 1

    # if not all elements in "valid_list" are "?",
    # convert "valid_list" to a string without delimiter
    # or,
    # assign a single "?" for both "valid_list" and "valid_result"
    # for easy handling in the future
    if count != len(valid_list):
        valid_result = "".join(valid_list)
    else:
        valid_list = ["?"]
        valid_result = "?"

    # convert "invalid_list" to a string with ", " as delimiter
    invalid_result = ", ".join(invalid_list)

    # print the translated message
    print("Translated message: ", valid_result, "\n")
    # print the invalid inputs if there is any
    if len(invalid_result) > 0:
        print("These morse codes were not able to be translated: ", invalid_result, "\n")

    return valid_list


# run demo function that fulfills the output requirement of Task3
if __name__ == '__main__':
    # declare a counter for loop control
    count = 0
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
            valid_list = process_input(user_input)

            # increment the counter after each loop
            count += 1
