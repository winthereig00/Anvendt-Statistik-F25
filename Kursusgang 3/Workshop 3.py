#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:24:57 2025

@author: lailawinthereig
"""

import pandas as pd
import numpy as np

"""
Exercise 4.12
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
Exercise 4.26
"""

numbers = np.array([12, 6, 22, 31, 23, 13, 15, 17, 21]) #Error in solution 21 is 31.

m_numbers = numbers.mean()
print("Mean from the numbers:", m_numbers)

variance = (sum((numbers-m_numbers)**2))/(len(numbers)-1)
print("Variance:", variance)

std_error = np.sqrt(variance)
print("Standard error", std_error)


"""
Exercise 4.37
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

#def fjong2(fjong(data, column_name)):
 #   return f'75% of the data lies between [{m-2*se,m+2*se}] and 88.9% lies between [{m-3*se,m+3*se}]'


#print(fjong2(fjong(data2, 'Speeds')))

# Combined function to calculate mean, variance, standard error, and ranges
def analyze_data(data, column_name):
    # Select the column from the DataFrame
    column_data = data[column_name]
    
    # Ensure the data is numeric and remove any non-numeric or NaN values
    column_data = pd.to_numeric(column_data, errors='coerce').dropna()
    
    # Calculate mean, variance (using pandas var function), and standard error
    mean = column_data.mean()
    variance = column_data.var(ddof=1)  # Sample variance
    standard_error = np.sqrt(variance)
    
    # Calculate the 75% and 88.9% ranges based on the mean and standard error
    range_75 = [mean - 2 * standard_error, mean + 2 * standard_error]
    range_889 = [mean - 3 * standard_error, mean + 3 * standard_error]
    
    # Return a formatted string with all the information
    return f"The mean is {mean}, the variance is {variance}, the standard error is {standard_error}, " \
           f"75% of the data lies between {range_75} and 88.9% lies between {range_889}"

# Call the function for the 'Speeds' column and print the result
result = analyze_data(data2, 'Speeds')
print(result)

