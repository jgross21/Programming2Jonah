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

file = open('data/super_villans.txt', 'r')  # Open file to read
print()
for line in file:
    print(line.strip())

file.close()

# You can make a new file by opening to write
file = open('data/oscars.txt', 'w')
file.write('Green Book\tBest Picture\n ')
file.close()

# better way to open and close a file

with open('data/super_villans.txt') as f:
    for line in f:
        print(line.strip())
    read_data = f.read() # big ol' string

# File automatically closes from with statement
print(read_data)

# Read data into a list (array)
with open('data/super_villans.txt') as f:
    villans = [x.strip() for  x in f]

print(villans)