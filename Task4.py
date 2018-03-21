#########################################
#                                       #
# This file takes the list of valid     #
# user input, "valid_list", from Task3, #
# analyze the occurrence of each        #
# character (both "A-Z" and "0-9")      #
# and print the result of analysis in   #
# the format of:                        #
#       Character: X                    #
#       Occurrence: #                   #
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

# import the list that contains the valid user input from Task3.py
from Task3 import valid_list

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
    "6": 0, "4": 7, "8": 0,
    "9": 0
}

# loop through the "valid_list", once detect a match with the key in "occ_dict",
# increment the corresponding value for 1
for valid_element in valid_list:
    if valid_element in occ_dict:
        occ_dict[valid_element] += 1

# loop through the "occ_dict" and print its elements properly
for keys, values in occ_dict.items():
    print('Character: ', keys)
    print('Occurrence: ', values, '\n')
