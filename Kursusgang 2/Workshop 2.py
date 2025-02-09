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


#Making a bar chart

## Select the columns to use as x and y data
x = data["Country"]
y = data["Oil_reserves"]

# Plot the bar chart
plt.bar(x, y)

# Rotate x-axis labels by 45 degrees
plt.xticks(rotation=90)

plt.xlabel('Country')
plt.ylabel('Oil Reserves')
plt.title("Bar Chart of Oil Reserves (Barrels) per Country")

plt.show()