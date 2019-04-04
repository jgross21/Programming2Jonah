# https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking/xq83-jr8c

'''
Energy Efficiency of Chicago Schools (35pts)
Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
We will use this data at the link above to look at schools.  
We will visualize the efficiency of schools by scatter plot.  
We hypothesize that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.
Make a scatterplot which does the following:  
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)

Challenge (for fun if you have time... not required):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)
'''

import csv
import matplotlib.pyplot as plt
import numpy as np

with open('Chicago_Energy_Benchmarking.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

schools_list = []
ghg_list = []
squrft_list = []
# Only Schools
for building in data:
    if building[6] == 'K-12 School':
        try:
            squrft = float(building[7])
            ghg = float(building[20])
            schools_list.append(building)
            ghg_list.append(ghg)
            squrft_list.append(squrft)
        except:
            print(building[0], building[2], 'threw an acception')


for item in schools_list:
    item[7] = float(item[7])
    item[20] = float(item[20])



otherlist = sorted(schools_list, key=lambda x: x[7]/x[20])
print(otherlist)

plt.figure(1)
# plotting
plt.scatter(squrft_list, ghg_list, color='red')

# labeling
plt.xlabel('Gross floor area (square feet)')
plt.ylabel('Total greenhouse gas emissions (metric tons)')
plt.title('Energy Emissions of Chicago K-12 Schools over 50,000 Sqare Feet')

# The annotations are hard to see.
# Parker
plt.annotate(data[3130][2], xy=(data[3130][7],data[3130][20]), color='darkblue') # Using a discussed technique

# Bottom 3
plt.annotate(otherlist[0][2], xy=(otherlist[0][7], otherlist[0][20]), color='red')
plt.annotate(otherlist[1][2], xy=(otherlist[1][7], otherlist[1][20]), color='red')
plt.annotate((otherlist[2][2]), xy=(otherlist[2][7], otherlist[2][20]), color='red')

# Top 3
plt.annotate(otherlist[-1][2], xy=(otherlist[-1][7], otherlist[-1][20]), color='lightgreen')
plt.annotate(otherlist[-2][2], xy=(otherlist[-2][7], otherlist[-2][20]), color='lightgreen')
plt.annotate(otherlist[-3][2], xy=(otherlist[-3][7], otherlist[-3][20]), color='lightgreen')

# Bestfit line # HOW DO I DO THIS???
m, b = np.polyfit(squrft_list, ghg_list, 1)
fitx = [50000, 0]
fity = [b, 50000 * m]

plt.plot(fitx,fity)

plt.show()

