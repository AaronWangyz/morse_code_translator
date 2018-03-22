#########################################
#                                       #
# This file declares a function called  #
# "take_input" that prompts a guide of  #
# input, takes user input, and returns  #
# it.                                   #
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
# Last Modified: March 22, 2018         #
#                                       #
#########################################


# declare a function that takes user input and return the input
def take_input():
    user_input = input("Please enter at least one morse code, "
                       "the morse code should be represent by 1 or 0, "
                       "each morse code should be separated "
                       "by a single asterisk (*): \n")
    return user_input
