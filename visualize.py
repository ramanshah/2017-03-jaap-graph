#! /usr/bin/env python

import csv
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 15})

with open('average_weekday_ridership.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    year, boardings = zip(*[(row['Year'], int(row['Boardings']))
                            for row in reader])

boardings_k = [boarding / 1000 for boarding in boardings]

plt.plot(year, boardings_k, 'bo-', markersize=10, clip_on=False)
plt.subplots_adjust(left=0.15, right=0.85, top=0.8, bottom=0.15)
plt.figtext(.5,.9,'Caltrain Average Weekday Ridership', fontsize=18, ha='center')
plt.figtext(.5,.85,'Source: Caltrain 2016 Annual Passenger Count',
            fontsize=13, ha='center')

plt.axis([1997, 2016, 0, 70])
plt.ylabel('Boardings (thousands)')
plt.yticks(range(0, 70, 20))
plt.xlabel('Year')
plt.xticks(range(2000, 2020, 5))

plt.annotate('{}: {:,}'.format(year[0], boardings[0]),
             xy=(year[0], boardings_k[0]),
             xytext=(10, -50),
             textcoords='offset points',
             arrowprops=dict(arrowstyle='->'))

plt.annotate('{}: {:,}'.format(year[-1], boardings[-1]),
             xy=(year[-1], boardings_k[-1]),
             xytext=(-150, -5),
             textcoords='offset points',
             arrowprops=dict(arrowstyle='->'))

plt.savefig('average_weekday_ridership.pdf')
