# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 19:47:18 2020

@author: harsh
"""

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("Internship_Project.csv") 

mean1= data['PARAMETER1'].mean()
print("\nMean Revenue: ""%.2f\n" % mean1)

data.query('PARAMETER1 < 400000', inplace = True)

print(data)

print("\nThe following cell sites fall under the category A, where Total Revenue is below Rs. 4,00,000.")

data.to_csv(r'C:\Users\harsh\.spyder-py3\A.csv',index=False)

x = data.PARAMETER1
y = data.PARAMTER2
plt.scatter(x, y)
plt.savefig("A.png")
