#  Exceptions

try:
    val = int(input('Enter a number: '))
except:
    print('You entered an invalid number')

# a better way to write it

done = False
while not done:
    try:
        val = int(input('Enter a number: '))
        done = True
    except:
        print('You entered an invalid number')

# Error types
try:
    int('a') # this line throws a value error
except ValueError:
    print('Value error')

# divide by zero
try:
    val = 3/0 # this produces a divided by zero error:
except ZeroDivisionError:
    print('You can\'t divide by zero')

# Input Output error
try:
    my_file = open('my_file.txt') # produces FileNotFoundError
except FileNotFoundError:
    print('file not found')

# Catch multiple errors
try:
    y = 10/0 # Catches the first one it runs into
    int('A')
except Exception as e:
    print('Exception caught')
    print(e)

# Make an MPG calculator

done = False
while not done:
    try:
        miles = float(input('Miles traveled:'))
        gallons = float(input('Gallons Used:'))
        done = True
    except:
        print('You entered an invalid number')

try:
    print('Your MPG:{:.2f}'.format(miles / gallons))
except:
    print('Your MPG is infinite')

# finally
try:
    my_file = open('my_file.txt', 'w')
    f = my_file.write('Hi')
    for line in f:
        print(line)
except:
    print('I/0 error')
finally:
    my_file.close()