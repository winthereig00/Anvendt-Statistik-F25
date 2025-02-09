#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:16:32 2025

@author: lailawinthereig
"""

"""
Workshop 2 - Exercise 2.13
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('https://raw.githubusercontent.com/winthereig00/Anvendt-Statistik-F25/main/Kursusgang%202/Xr02-13.xlsx')

data.head #Giving us a look at the data

#We now seek to rename one of the columns

data.rename(columns = {'Oil Reserves (Barrels)' : 'Oil_reserves'}, inplace=True)

#print(data)

#Making a bar chart

## Select the columns to use as x and y data
x = data["Country"]
y = data["Oil_reserves"]

# Plot the bar chart
plt.bar(x, y)

# Rotate x-axis labels by 90 degrees
plt.xticks(rotation=90)

plt.xlabel('Country')
plt.ylabel('Oil Reserves')
plt.title("Bar Chart of Oil Reserves (Barrels) per Country")

#plt.show()

"""
Exercise 2.14 - Make a pie chart!
"""

#Renaming some of the countries
data["Country"] = data["Country"].replace({
    "United States": "USA",
    "United Arab Emirates": "UAE",
})

#Calculate the percentafes for a pie chart
#Making a piechart

# Calculate total and create a list of percentages
total = data['Oil_reserves'].sum()
percentages = 100 * data['Oil_reserves'] / total

# Plot the pie chart
plt.pie(percentages, labels=data['Country'], autopct='%1.1f%%', pctdistance=0.8)
plt.axis('equal')
#plt.show()


"""
Exercise 2.15 - Make a bar chart and a pie chart from a new file
"""

data2 = pd.read_excel('https://raw.githubusercontent.com/winthereig00/Anvendt-Statistik-F25/main/Kursusgang%202/Xr02-15.xlsx')

data2.rename(columns = {'Consumption of oil (barrels per day)' : 'Consumption'}, inplace=True)

print(data2)



#Bar chart:
x = data2["Country"]
y = data2["Consumption"]

#Without the figsize command, the plot does not work, probably because there are a lot of factors.
plt.figure(figsize=(10, 6))  # Increase figure size to fit the labels
plt.bar(x,y)

plt.xticks(rotation=90)  # Rotate x labels if needed for readability

plt.xlabel("Country")
plt.ylabel("Consumption")
plt.title("Oil Consumption per Country")

plt.show()

#Pie Chart
total2 = data2['Consumption'].sum()
percentages2 = 100*data2['Consumption'] / total2

plt.pie(percentages2, labels = data2['Country'], autopct='%1.1f%%', pctdistance=0.8)
plt.axis('equal')
plt.show()



