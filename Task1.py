#######################################################################
#                                                                     #
# This file contains a morse code dictionary called "morse_dict" that #
# will be used in Task3.py, and a function called "print_structure"   #
# that will be used in Task4.py and the demo function here in this    #
# file.
#                                                                     #
#######################################################################
#                                                                     #
# The program was implemented in python 3.6.4, under PyCharm Edu IDE. #
#                                                                     #
#######################################################################
#                                                                     #
#                               Usage                                 #
# Simply execute this script, the structure of "morse_dict" will be   #
# displayed.                                                          #
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

# declare a dictionary contains the morse code (in 1 and 0s)
# as the "key", and the corresponding English letter or number
# as the "value"
morse_dict = {

    # 26 English letters
    '01': 'A',     '1000': 'B',    '1010': 'C',
    '100': 'D',    '0': 'E',       '0010': 'F',
    '110': 'G',    '0000': 'H',    '00': 'I',
    '0111': 'J',   '101': 'K',     '0100': 'L',
    '11': 'M',     '10': 'N',      '111': 'O',
    '0110': 'P',   '1101': 'Q',    '010': 'R',
    '000': 'S',    '1': 'T',       '001': 'U',
    '0001': 'V',   '011': 'W',     '1001': 'X',
    '1011': 'Y',   '1100': 'Z',

    # 10 numbers
    '11111': '0', '01111': '1', '00111': '2',
    '00011': '3', '00001': '4', '00000': '5',
    '10000': '6', '11000': '7', '11100': '8',
    '11110': '9'
}


# print the morse code representation structure
def print_structure():
    print("Structure of morse_dict: ")
    for keys, values in morse_dict.items():
        print('Morse Code: ', keys)
        print('Value: ', values, "\n")


# make this file executable
if __name__ == "__main__":
    print_structure()
