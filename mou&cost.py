# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:34:50 2020
@author: harsh
"""

#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
import pandas as pd
data=pd.read_csv("Internship_Project.csv") 

data.query('PARAMETER3 ==0 and PARAMETER1 < PARAMTER2', inplace = True)

#x=data.count()
print(data)
total1= data['PARAMETER1'].sum()
total2= data['PARAMTER2'].sum()

print('Total Revenue: '"%.2f" % total1)
print('Total Cost: '"%.2f" % total2)
print('Minutes of Usage: 0')
print('The following Cell Sites should be made Non-functional.')

#data.to_csv(r'C:\Users\harsh\.spyder-py3\mou.csv',index=False)

#plt.figure(figsize=(50,50))

#x = data.PARAMETER1
#y = data.PARAMTER2
#plt.scatter(x, y)
#plt.savefig("mou.png")

#data.plot.pie(subplots=True)
#data.plot.bar(y=['PARAMETER1','PARAMTER2'], x='Site_ID')