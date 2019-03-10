'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''

# This function takes in a line of text and returns
# a list of words in the line.
import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

# Arraying the chapter
file = open('dictionary.txt', 'r')

dictionary_list = []
for line in file:
    line = line.strip()
    dictionary_list.append(line)

file.close()

print('--- Linear Search ---')


file = open('AliceInWonderLand200.txt')
line_number = 0

for line in file:
    line = line.strip().upper()
    line_number += 1
    words = split_line(line)
    for word in words:
        i = 0
        while i < (len(dictionary_list)) and word != dictionary_list[i]:
            i += 1
        if i >= len(dictionary_list):
            print('Found', word, 'mispelled at line', line_number)

file.close()


print('--- Binary Search ---')

file = open('AliceInWonderLand200.txt')
line_number = 0

for line in file:
    line = line.strip().upper()
    line_number += 1
    words = split_line(line)
    for word in words:
        lower_bound = 0
        upper_bound = len(dictionary_list)
        found = False
        key = word.upper()

        while lower_bound <= upper_bound and not found:
            middle_pos = (upper_bound + lower_bound) // 2
            if dictionary_list[middle_pos] < key:
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > key:
                upper_bound = middle_pos - 1
            else:
                found = True
        if not found:
            print('Found', word, 'mispelled at line', line_number)

file.close()
