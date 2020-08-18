# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:27:25 2020

@author: harsh
"""

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("Pied.csv", index_col=0)
data.plot.pie(figsize=(8,8),autopct = "%.2f%%",colors = ['red', 'orange','green'],subplots=True)
plt.savefig("pied.png")
