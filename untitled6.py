# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:17:56 2025

@author: sarit
"""

# Categorize gender
df['Gender'] = df['Gender'].map({'M' : 0,
                                 'F' : 1, }).astype(float)
#Display data
df

 # Code continued from Hacker Store Official 