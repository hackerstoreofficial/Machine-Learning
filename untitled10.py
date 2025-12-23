# -*- coding: utf-8 -*-
"""
Spyder Editor

Creation and Loading different datasets in Python
"""

# Import pandas package
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
#df.head()
#df.tail()