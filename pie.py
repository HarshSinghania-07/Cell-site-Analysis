# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:45:29 2020

@author: harsh
"""
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("Pie.csv", index_col=0)
data.plot.pie(figsize=(8,8),autopct = "%.2f%%",colors = ['green', 'blue','yellow'],subplots=True)
plt.savefig("pie.png")
