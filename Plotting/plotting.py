# plotting with matplotlib

import matplotlib.pyplot as plt

plt.figure(1) # creates a new window

plt.plot([1, 2, 3, 4]) # if no x axis, just uses the index
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.figure(2, facecolor='lightblue')
x = [x for x in range(100)]
y = [y ** 2 for y in range (100)]

plt.plot(x, y, color='green', marker='^', markersize = 10, linestyle='--')

plt.xlabel('x label (units)')
plt.ylabel('y label (units)', color='green', fontsize=15)
plt.title('Example Plot', color='blue', fontsize=20)
plt.axis([10, 20, 100, 500]) # xmin, xmax, ymin, ymax

# plt.show()

import matplotlib.pyplot as plt
import csv

with open('/Users/jonahgross/PycharmProjects/Programming2_SP19/Plotting/Libraries_-_2018_Visitors_by_Location.csv') as f:
    reader = csv.reader(f) # create a reader object from a csv lib
    data = list(reader) # casts it as a list

print(reader)

month_numbers = [x for x in range (12)] # Month numbers on x

library_names = [x[0] for x in data[1:]] # Month names on x
# print(library_names)

header = data.pop(0)

# print(header)

month_data = [x[1:-1] for x in data] # Jan to Dec data for all libraries.
# print(month_data[0])

plt.figure(3, tight_layout=True)  # Allows data to fit axes

library_data = [int(x) for x in month_data[library_names.index('Lincoln Park')]]
plt.bar(month_numbers, library_data)
plt.title('Lincoln Park Library - Visitors by Month 2018')
plt.xlabel('Month')
plt.ylabel('Visitors')

month_names = header[1:-1]
plt.xticks(month_numbers, month_names, rotation=45, fontsize=8) # Replaces number with labels


# Make a graph of all library
plt.figure(4, tight_layout=True, figsize=(8, 6), facecolor='lightblue')

all_lib_months = [0 for x in range(12)]

for library in month_data:
    for i in range(12):
        all_lib_months[i] += int(library[i])

plt.bar(month_numbers, all_lib_months, color='red', label='mylabel')
plt.xticks(month_numbers, month_names, rotation=60)
plt.xlabel('Months')
plt.ylabel('Visitors')
plt.title('Chicago Library Visitors by Month (2018')

plt.legend()

plt.show()