# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:09:33 2020

@author: harsh
"""

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("Internship_Project.csv") 

mean1= data['PARAMETER1'].mean()
print("\nMean Revenue: ""%.2f\n" % mean1)

data.query('PARAMETER1 > 400000 and PARAMETER1 < 1000000', inplace = True)

print(data)

print("\nThe following cell sites fall under the category B, where Total Revenue is between Rs. 4,00,000 and Rs. 10,00,000.")

data.to_csv(r'C:\Users\harsh\.spyder-py3\B.csv',index=False)

x = data.PARAMETER1
y = data.PARAMTER2
plt.scatter(x, y)
plt.savefig("B.png")