#######################################################################
#                                                                     #
# This file declares a function that will be used in Task2.py called  #
# "take_input" that prompts a guide of input, takes user input, and   #
# returns it.                                                         #
#                                                                     #
# Function "recursive_input" is also implemented in this file which is#
# to fulfill the output requirements for Task2.                       #
#                                                                     #
#######################################################################
#                                                                     #
# The program was implemented in python 3.6.4, under PyCharm Edu IDE. #
#                                                                     #
#######################################################################
#                                                                     #
#                               Usage                                 #
# The program will prompt for user input after the file is executed,  #
# the user is allowed to keep enter contents until an empty input is  #
# received which is considered as the sign of end of input.           #
#                                                                     #
# Regular expression is introduced in this stage to limit #the user   #
# action. The allowed inputs from user are limited in 1, 0 and *, plus#
# user has to follow the pattern of                                   #
#               "digit(s)*digit(s)*digit(s)......(*)"                 #
# which means one and only one asterisk is allowed as delimiter.      #
#                                                                     #
# The program also displays the content received from user every time #
# user entered something and hit "Enter".                             #
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

import re


# declare a function that takes user input and return the input
# this is the function that will be used in Task3.py and Task4.py
def take_input():
    user_input = input("Please enter at least one morse code, "
                       "the morse code should be represent by 1 or 0, "
                       "each morse code should be separated "
                       "by a single asterisk (*): \n")
    return user_input


# demo function to fulfill the output requirement of Task2
def recursive_input():

    # regexp variable for input check
    valid_input = "^([01]+\*?)+$"

    # take user input until empty input is received
    while True:
        user_input = take_input()

        # stop the loop if empty string is received
        if user_input == "":
            break

        # validate the input if input is not empty
        elif not re.match(valid_input, user_input):
            while True:
                user_input = input("Invalid input! Please re-enter: \n")
                if re.match(valid_input, user_input):
                    print("\nYou entered: ", user_input, "\n")
                    break
                elif user_input == "":
                    quit()

        # print the valid input
        else:
            print("You entered: ", user_input)


# run demo function
if __name__ == "__main__":
    recursive_input()
