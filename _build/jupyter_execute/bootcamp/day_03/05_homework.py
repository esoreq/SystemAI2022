#!/usr/bin/env python
# coding: utf-8

# ## DAY 03 - HOMEWORK 
# 
# - Solve as many of the exercises below 

# ### Exercise 1: Calculate age
# - Write a function that takes date of birth as an argument, and returns the age in years.

# ### Exercise 2: Treat negative numbers differently 
# - Write a function that takes as an input a single number
# - And returns a transformed number such as 
#   - For negative numbers 1/number
#   - For positive numbers the number squared 
#   - And if the number is not a number it prints an error and returns the string `NaN`

# ### Exercise 3: calculations 
# - Write a function that gets two numbers 
# - and returns the addition, subtraction multiplication and division of these numbers
# - For example if we give the function the numbers 3,2 we will get 5,1,6,1.5
# 

# ### Exercise 4: Create a function with variable length of arguments
# - Write a function that takes as an input any set of arguments
# - And returns a transformed set of numbers such as 
#   - Positive sum
#   - Negative sum
#   - non-numbers count
# 
# For example if we give you function the following input 
# ~~~python
# args = [10,-50,7,9,-20,'a','null','5']
# ~~~
# - It will return 26,-70,3

# ### Exercise 5: Using the same type of input filter conditionally 
# - Write a function that takes as an input any set of arguments
# - And returns a filtered set of values in a list 
#   - return only Positive numbers
#   - return only Negative numbers
#   - return any number (even if in string format) 
#   - return only non-numbers
# 
# For example if we give you function the following input 
# ~~~python
# args = [10,-50,7,9,-20,'a','null','5']
# condition = 'numbers'
# ~~~
# - It will return [10, -50, 7, 9, -20, 5]

# ### Exercise 6: Using the same type of input use map to clean input 
# - Write a function that takes as an input any set of arguments
# - And returns a mapped set of values in a list where
#   - all numbers are of type float
#   - all non-numbers are transformed into 'NaN'
# 
# For example if we give you function the following input 
# ~~~python
# args = [10,-50,7,9,-20,'a','null','5']
# ~~~
# - It will return [10, -50, 7, 9, -20,'NaN','NaN', 5]
