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
# try to translate the morse code entered by user (assuming user are  #
# actually entering morse codes), display the translated message, and #
# list the user inputs that were not translatable.                    #
#                                                                     #
# In this stage, untranslatable inputs will be displayed as "?" in    #
# the translated message.                                             #
#                                                                     #
#######################################################################
#                                                                     #
# Author: Yezhen Wang                                                 #
# Student ID: 2861 9943                                               #
# Email: ywan0072@student.monash.edu                                  #
# Date Created: March 21, 2018                                        #
# Last Modified: March 23, 2018, 01:38 PM                             #
#                                                                     #
#######################################################################

# import morse_dict and user_input from previous python files
from Task1 import morse_dict
import Task2


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
    while True:
        # assign the return value of Task2.take_input (should just be an input from user)
        # to "user_input" variable
        demo_input = Task2.take_input()

        # check if user input is empty string,
        # stop the loop if it is
        if demo_input == "":
            break

        # translate the user input if its not empty
        else:
            print("\nYou entered: ", demo_input, "\n")
            process_input(demo_input)
