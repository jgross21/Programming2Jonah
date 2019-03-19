# Universal Gravity Calculator (15pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters


# Make a calculator that does all of the following 
# (3pts) takes the inputs for mass 1, mass 2.and distance between the two objects (m1, m2, and r) 
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (3pts) keeps asking for inputs until they are valid (see while loop from notes)
# (4pts) calculate the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.

# m1
done = False
while not done:
    try:
        m1 = int(input('What\'s your first mass in kg?'))
        print()
        done = True
    except:
        print('You entered an invalid number.')
        print()

# m2
done = False
while not done:
    try:
        m2 = int(input('What\'s your second mass in kg?'))
        print()
        done = True
    except:
        print('You entered an invalid number.')
        print()
# r
done = False
while not done:
    try:
        r = int(input('What\'s your distance between the centers of the two masses?'))
        print()
        done = True
    except:
        print('You entered an invalid number.')
        print()
g = 6.67e-11
try:
    f = g * (m1 * m2) / r ** 2
except:
    print('Something has gone wrong')


print('That is {:.2e}'.format(f), 'newtons.')