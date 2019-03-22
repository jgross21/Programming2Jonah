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

plt.show()