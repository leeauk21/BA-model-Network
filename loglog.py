# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:06:39 2020

@author: Ching Hoe Lee
"""
import numpy as np
import matplotlib.pyplot as plt
from logbin230119 import logbin
deg_list=np.loadtxt('degree_list.txt',dtype=int)
i=0
x=np.unique(deg_list[i])
y=np.unique(deg_list[i],return_counts=True)[1]/100000
plt.loglog(x,y,'x',label='raw data')
a,b=logbin(deg_list[i],scale=1.5,zeros=False)
plt.loglog(a,b,'--',label='log binned data')
plt.legend()
plt.xlabel('log k')
plt.ylabel('log P(k)')
plt.savefig('logbin.png')
plt.show()
