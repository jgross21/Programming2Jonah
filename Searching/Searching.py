file = open('data/super_villans.txt', 'r')  # Open file to read

print(file)

'''
for line in file:
    print(line.strip()) # Strip method removes any extra spaces, \t, \n
'''

for line in file:
    print('Hello', line.strip())  # You can only read through one time

file.close()  # ends your access to file

# Open a file to write (Overwrites all previous)
'''
file = open('data/super_villans.txt', 'w')  # Open file to write
file.write('Lee the Merciless\n')
file.close()

file = open('data/super_villans.txt', 'r')  # Open file to read
for line in file:
    print(line.strip()) # Strip method removes any extra spaces, \t, \n

file.close()
# THIS REMOVES EVERYTHING
'''

# Open a file to append(does not overwrite)
file = open('data/super_villans.txt', 'a')  # Open file to append
file.write('Dan the Man\n')
file.close()

file = open('Data/super_villans.txt', 'r')  # Open file to read
print()
for line in file:
    print(line.strip())

file.close()

# You can make a new file by opening to write
file = open('Data/oscars.txt', 'w')
file.write('Green Book\tBest Picture\n ')
file.close()

# better way to open and close a file

with open('Data/super_villans.txt') as f:
    for line in f:
        print(line.strip())
    read_data = f.read() # big ol' string

# File automatically closes from with statement
print(read_data)

# Read data into a list (array)
with open('Data/super_villans.txt') as f:
    villans = [x.strip().upper() for  x in f]

print(villans)

# Linear Search
print(villans.index('RENARD THE TORTURER'))

key = 'YASMIN DEL CORVIDA'
i = 0 # the index of my search

while i < (len(villans) - 1) and key != villans[i]:
    i += 1

if i < len(villans):
    print('Found', key, 'at position', i)
else:print('Could not find key')

# Binary Search
villans.sort()

key = 'THEODORA THE WICKED'
lower_bound = 0
upper_bound = len(villans)
found = False
loops = 0

# Loop until we find it

while lower_bound <= upper_bound and not found:
    middle_pos = (upper_bound + lower_bound) // 2
    loops += 1
    if villans[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villans[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True
if found:
    print(key, 'was found at position', middle_pos, 'after', loops, 'loops')
else:
    print('Key was not found')

import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

text = 'Hello, this is Alexa\'s phone'

line = split_line(text)
print(line)

file = open('Data/super_villans.txt')

for line in file:
    line = line.strip()
    words = split_line(line)
    for word in words:
        print(word)