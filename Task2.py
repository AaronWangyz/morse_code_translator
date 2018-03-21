#########################################
#                                       #
# This file declares a regexp variable  #
# that is used to validate user input,  #
# if the input is invalid, the program  #
# asks user to re-enter until it is     #
# valid.                                #
#                                       #
#########################################
#                                       #
# The program was implemented in        #
# python 3.6.4, under PyCharm Edu IDE.  #
#                                       #
#########################################
#                                       #
# Author: Yezhen Wang                   #
# Student ID: 2861 9943                 #
# Email: ywan0072@student.monash.edu    #
# Date Created: March 21, 2018          #
# Last Modified: March 21, 2018         #
#                                       #
#########################################

import re

# declare a variable contains the regexp of the valid input
# the regexp will only take the format as follows:
# 0-n 0 or 1s with a * separates them, the pattern appears at least one time

# !!!want to improve the regexp here!!!
valid_input = "^([01]+\*?)+$"

# while the user input does not match the regexp of the valid input, ask user to re-enter:
while True:
    user_input = input("Please enter at least one morse code, "
                       "the morse code should be represent by 1 or 0, "
                       "each morse code should be separated "
                       "by a single asterisk (*): ")
    if re.match(valid_input, user_input):
        print("You entered: ", user_input, "\n\n")
        break
    else:
        print("Invalid input! Please re-enter: \n")
