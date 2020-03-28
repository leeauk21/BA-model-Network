# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:16:33 2020

@author: Ching Hoe Lee
"""
import numpy as np
from scipy.stats import chisquare
from logbin230119 import logbin
import matplotlib.pyplot as plt
from net_project import project
N=[100,1000,10000,20000,30000,40000,50000]
m=3
num=10

y=[]
std=[]
theory_y=[]
for i in N:
   j=0
   sample=[]
   while j<num:
      new=project(m+1,i)
      new.ran_attach(m)
      max_k=np.max(new.degree())
      sample.append(max_k)
      j+=1
   y.append(np.mean(sample))
   std.append(np.std(sample))
   theory=m-(np.log(1*i))/(np.log(m/(m+1)))
      #1.5 should be 2
   theory_y.append(theory)

plt.errorbar(N,y,yerr=std,fmt='x',label='data')
plt.plot(N,theory_y,'+',label='theoretical prediction')
plt.xlabel('N')
plt.ylabel('Maximum Degree')
plt.legend()
plt.savefig('new.png')
plt.show()
chi=chisquare(y,f_exp=theory_y,ddof=1)
print(chi)