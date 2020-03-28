# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:57:09 2020

@author: Ching Hoe Lee
"""

import numpy as np
from logbin230119 import logbin
import matplotlib.pyplot as plt
from net_project import project
from scipy.stats import chisquare
m=[3,9,27]
chisq=[]
for i in m:
   new=project(i+1,10000)
   new.ran_attach(i)
   x,y=logbin(new.degree(),scale=1.08,zeros=False)
   plt.loglog(x,y,'x',label=f'm={i}')
   power=x-i
   p=i**(power)/(i+1)**(power+1)
   plt.loglog(x,p)
   chisq.append(chisquare(p,f_exp=y,ddof=1))
   #cant compute for higher m
plt.ylabel('log P(k)')
plt.xlabel('log k')
plt.legend()
plt.savefig('random_degree_distribution')
plt.show()
   