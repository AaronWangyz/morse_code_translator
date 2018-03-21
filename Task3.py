#########################################
#                                       #
# This file takes the morse_dict built  #
# in Task1.py and user_input received   #
# from Task2.py by import function.     #
# Then split the user_input by "*"      #
# and translate the morse code entered  #
# by user to the corresponding message. #
#                                       #
# The invalid morse code entered will   #
# be translated as "?" and printed out  #
# after the message.                    #
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

# import morse_dict and user_input from previous python files
from Task1 import morse_dict
from Task2 import user_input

# declare lists for storing valid and invalid user input
valid_list = []
invalid_list = []
# declare variables for storing the final outputs
valid_result = ""
invalid_result = ""
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
        valid_list.append("?")
        if split_element not in invalid_list:
            invalid_list.append(split_element)

# convert "valid_list" to a string without delimiter
valid_result = "".join(valid_list)
# convert "invalid_list" to a string with ", " as delimiter
invalid_result = ", ".join(invalid_list)

# print the translated message
print("Translated message: ", valid_result, "\n\n")
# print the invalid inputs if there is any
if len(invalid_result) > 0:
    print("These morse codes were not able to be translated: ", invalid_result, "\n\n")
