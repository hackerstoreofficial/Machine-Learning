# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:15:02 2025

@author: sarit
"""

#Import pandas package
import pandas as pd

# Assign data
data = {'Name' : ['Jai', 'Yogendra', 'Ravi', 'Yogesh', 'Devesh', 'Sumit', 'Vishal'],
'Age' : [17, 17, 18, 17, 21, 20, 21],
'Gender' : ['M', 'M', 'F', 'M', 'M', 'F', 'F'],
'Marks' : [90,76, 'NaN', 39, 99, 'NaN', 71]}

# Convert into DataFrame
df = pd.DataFrame(data)
# Display data
print(df)

# Code continued from Hacker Store Official