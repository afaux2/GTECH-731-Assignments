# GTECH 731 Assignment 1

# Task 1 --------------------------------------------------

import platform
from statistics import variance
import statistics
print(platform.python_version())

# Task 2 --------------------------------------------------

# Generate a list of random numbers using random module in Python

import random
random.seed(5)
random_list = random.sample(range(0, 100), 20)
print(random_list)

# Calculate the mean value for the list by looping through its elements


for number in random_list:
    # Calculate sum of list
    list_sum = sum(random_list)
    
    # Calculate mean
    list_mean = list_sum / len(random_list)
    print('the mean of the list is', list_mean)

# Calculate the variance of the list

list_variance = statistics.variance(random_list)
print(list_variance) 




