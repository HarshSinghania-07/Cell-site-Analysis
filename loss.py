# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:22:18 2020

@author: harsh
"""

import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
data=pd.read_csv("Internship_Project.csv") 
data.query('PARAMETER1 < PARAMTER2', inplace = True)

print(data)

#Calculating Mean of Total Revenue and Cost
mean1 = data['PARAMETER1'].mean()
print('Mean Revenue: '"%.2f" % mean1)
mean2 = data['PARAMTER2'].mean()
print('Mean Cost: '"%.2f" % mean2)

#Calculating Sum of Total Revenue and Cost
total1= data['PARAMETER1'].sum()
total2= data['PARAMTER2'].sum()

#Calculating Loss 
loss= total2 - total1
print('Loss occured: '"%.2f" % loss)
print('\nThe following Cell Sites are suffering a loss.')

#Storing the filtered data to a new csv file
data.to_csv(r'C:\Users\harsh\.spyder-py3\loss.csv',index=False)


x = data.PARAMETER1
y = data.PARAMTER2
plt.scatter(x, y)
plt.savefig("loss.png")