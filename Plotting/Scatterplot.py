import csv
import matplotlib.pyplot as plt
import numpy as np

with open('guns.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)

print(data)

header = data.pop(0)
print(header)

# make a scatter of firearms per 100 vs homicides per 100k
homicide_100k = []
firearms_100 = []
countries = ['United States', 'New Zealand', 'Canada', 'Mexico', 'South Korea', 'Japan', 'England and Wales', 'Netherlands', 'France', 'South Africa', 'Nigeria', 'Germany', 'Taiwan', 'Singapore', 'Denmark', 'Iceland', 'Switzerland', 'Spain', 'Sweden', 'Hungary']

for country in data:
    if country[0] in countries:
        try:
            homicides = float(country[5])
            firearms = float(country[-2])
            name = country[0]
            homicide_100k.append(homicides)
            firearms_100.append(firearms)
            countries.append(name)
        except:
            print(country[0], 'has inadequate data')

print(countries)
plt.figure(1)
plt.scatter(firearms_100, homicide_100k)
plt.ylabel('Homicides per 100k people')
plt.ylabel('Firearms per 100 people')

# Make a best-fit line
m, b = np.polyfit(firearms_100, homicide_100k, 1)

fitx = [0, 100]
fity = [b, 100 * m]
plt.plot(fitx, fity)

plt.show()

