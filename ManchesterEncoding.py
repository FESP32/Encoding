import matplotlib.pyplot as plt
import numpy as np

CONST_MANCHESTER_ZERO = '01'
CONST_MANCHESTER_ONE = '10'


def letter_bin_code(character):
    final_string = ''
    for c in character:
        ascii_character = ord(c)
        final_string += "{0:b}".format(ascii_character)
    return final_string


def manchester_encoding(binstring):
    manchester_string = ''
    binstring = str(binstring)

    for c in binstring:
        if c == '0':
            manchester_string += CONST_MANCHESTER_ZERO
        elif c == '1':
            manchester_string += CONST_MANCHESTER_ONE
        else:
            print 'a non binary symbol has been found, retype your binary string'
            return

    return manchester_string


def binarystring_to_list(string):
    string_list = []
    for c in string:
        string_list.append(int(c))

    return string_list

user_input = raw_input('insert your character string: ')

encoded_data = binarystring_to_list(manchester_encoding(letter_bin_code(user_input)))

x = np.arange(1, len(encoded_data) + 1, 1)

#

plt.step(x, encoded_data)
plt.xlim(0, len(encoded_data) + 1)
plt.ylim(-1, 2)
plt.title('Manchester Encoding')
plt.show()

