#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:24:57 2025

@author: lailawinthereig
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



"""
#Exercise 4.12
"""

data = pd.read_excel("https://raw.githubusercontent.com/winthereig00/Anvendt-Statistik-F25/main/Kursusgang%203/Xr04-12.xlsx")

print(data)

total = len(data)
mean = data['Commute time'].sum() / total

print(mean)

mean2 = data['Commute time'].mean()
print('Mean: ', mean2)

median = data['Commute time'].median()
print('Median: ', median)

mode = data['Commute time'].mode().get(0) #Using .get(0) to retrieve the first mode value 
print('Mode:', mode)


"""
#Exercise 4.26
"""

numbers = np.array([12, 6, 22, 31, 23, 13, 15, 17, 21]) #Error in solution 21 is 31.

m_numbers = numbers.mean()
print("Mean from the numbers:", m_numbers)

variance = (sum((numbers-m_numbers)**2))/(len(numbers)-1)
print("Variance:", variance)

std_error = np.sqrt(variance)
print("Standard error", std_error)


"""
#Exercise 4.37
"""

data2 = pd.read_excel("https://raw.githubusercontent.com/winthereig00/Anvendt-Statistik-F25/main/Kursusgang%203/Xr04-37.xlsx")

print(data2)

def fjong(data, column_name):
    column_data = data[column_name]
    
    m = column_data.mean()
    v = (sum((column_data-m)**2))/(len(column_data)-1)
    se = np.sqrt(v)

    return f'The mean is {m}, the variance is {v} and the standard error is {se}'


print(fjong(data2, 'Speeds'))


"""
#Exercise 4.71
"""

data3 = pd.read_excel("https://raw.githubusercontent.com/winthereig00/Anvendt-Statistik-F25/main/Kursusgang%203/Xr04-71.xlsx")

print(data3)

percentiles = data3['Times'].quantile([0.25, 0.5, 0.75]) #The quantile() method in pandas is used to compute the value at a specific percentile (or quantile) in a dataset.

first_quartile = percentiles[0.25]
print("First Quartile: ", first_quartile)

median = percentiles[0.5]
print("Second Quartile: ", median)

third_quartile = percentiles[0.75]
print("Third Quartile: ", third_quartile)

# plot the data and measures on a histogram
plt.hist(data3['Times'], bins=20, edgecolor='black', alpha=0.5, density=True) #Density=True gives percentages

plt.axvline(first_quartile, color='red', label='1st Quartile')
plt.axvline(median, color='green', label='Median')
plt.axvline(third_quartile, color='red', label='3rd Quartile')
plt.legend()
plt.show()



"""
Exercise 4.83
"""

data4 = pd.read_excel("https://raw.githubusercontent.com/winthereig00/Anvendt-Statistik-F25/main/Kursusgang%203/Xr04-83.xlsx")

print(data4)

# Calculate covariance
covariance = data4.cov().loc["Study time", "Marks"]
print("Covariance:", covariance)

# Calculate coefficient of correlation
correlation = data4.corr().loc["Study time", "Marks"]
print("Coefficient of correlation:", correlation)

determination = correlation**2
print("Coefficient of determination:", determination)

#Visualise the data
## Select the columns to use as x and y data
x = data4["Study time"]
y = data4["Marks"]

# Plot the data
plt.scatter(x,y)
plt.xlabel("Study time")
plt.ylabel("Marks")
plt.title("Study time vs. Marks")
plt.show()

#We know want to make the plot with the regression line using least squares method:

marks_mean = data4["Marks"].mean()
study_mean = data4["Study time"].mean()

num = ((data4["Study time"] - study_mean) * data4["Marks"]).sum()
den = ((data4["Study time"] - study_mean)**2).sum()

#print(np.array([(data4["Study time"] - study_mean), (data4["Marks"] - marks_mean)]))

slope = num / den
print("Slope:", slope)

intercept = marks_mean - slope * study_mean #We know the means are on the regression line
print("Intercept:", intercept)

# Use the line to make predictions
predictions = intercept + slope * data4["Study time"]

# Plot the data
plt.scatter(x,y)

# Plot the line
plt.plot(data4["Study time"], predictions, color='red')
plt.xlabel("Study time")
plt.ylabel("Marks")
plt.title("Study time vs. Marks")

# Show the plot
plt.show()




