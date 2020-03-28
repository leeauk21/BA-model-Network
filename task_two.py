# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:02:12 2020

@author: Ching Hoe Lee
"""

from logbin230119 import logbin
import numpy as np
import matplotlib.pyplot as plt
from net_project import project
from scipy.stats import chisquare
N=100000
m=[4,16,64,256]
deg_list=np.loadtxt('degree_list.txt',dtype=int)
i=0
chisq=[]
while i < len(m):
   x,y=logbin(deg_list[i],scale=1.1,zeros=False)
   p=2*m[i]*(m[i]+1)/(x*(x+1)*(x+2))
   plt.loglog(x,p,label=f'm={m[i]}')
   plt.loglog(x,y,'x',label=f'm={m[i]}')
   chisq.append(chisquare(p,f_exp=y,ddof=1))
   i+=1
   
plt.xlabel("log k")
plt.ylabel("log P(k)")
plt.legend()
plt.savefig('deg_plot.png')
plt.show()