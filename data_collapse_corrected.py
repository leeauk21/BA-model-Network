# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:14:42 2020

@author: Ching Hoe Lee
"""
import numpy as np
from logbin230119 import logbin
import matplotlib.pyplot as plt
from net_project import project
"need to take average"
k_one=np.loadtxt('k_one.txt')
m=3
N=[100000,200000,400000,600000,800000,1000000]
k_one_mean=np.mean(k_one,axis=1)
i=0
for i in N:
      new=project(m+1,i)
      new.pref_attach(m)
      x,y=logbin(new.degree(),scale=1.6,zeros=False)
      p=2*m*(m+1)/(x*(x+1)*(x+2))
      plt.loglog(x/np.sqrt(i),y/p,label=f'N={i}')
plt.xlabel('β')
plt.ylabel('α')
plt.legend()
plt.savefig('data_collapse_two.png')
plt.show()
