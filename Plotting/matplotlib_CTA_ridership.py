# CTA Ridership (28pts)

#  Get the csv from the following data set.
#  https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
#  This shows CTA ridership by year going back to the 80s

import matplotlib.pyplot as plt
import csv

with open('CTA_-_Ridership_-_Annual_Boarding_Totals.csv') as f:
    reader = csv.reader(f) # create a reader object from a csv lib
    data = list(reader)

#1  Make a plot of rail usage for the most current 10 year period.  (year on x axis, and ridership on y) (5pts)

plt.figure(1, tight_layout=True)

rails = [float(x[3]) for x in data[-10:]]
years = [x[0] for x in data[-10:]]
print(years)
print(rails)
plt.plot(years, rails, label='Train riders')

plt.ylabel('Hundreds of Millions of Riders')
plt.xlabel('Year')
plt.title('CTA train ridership: 2008-2017')

#2  Plot bus usage for the same years as a second line on your graph. (5pts)

bus = [float(x[1]) for x in data[-10:]]
plt.plot(years, bus, label='Bus riders')

#3  Plot bus and rail usage together on a third line on your graph. (5pts)

total = [float(x[4]) for x in data[-10:]]
plt.plot(years, total, label='Total riders')

#4  Add a title and label your axes. (5pts)

plt.ylabel('Hundreds of Millions of Riders')
plt.xlabel('Year')
plt.title('CTA train ridership: 2008-2017')

#5  Add a legend to show data represented by each of the three lines. (5pts)

plt.legend()

#6  What trend or trends do you see in the data?  Offer at least two hypotheses which might explain the trend(s). (3pts)
# I see that total bus riders has consistently gone down over the past decade. On the contrary, train usage has slightly gone up.
# Overall, total transit usage has gone down. This may be because of the rising popularity of ridesharing apps that are much more convenient
# than public transit. The increase in train usage may be due to the fact that people see the train as scenic and an essential Chicago
# experience, and many people want to see it.

plt.show()