# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:33:43 2020

@author: Ching Hoe Lee
"""
import numpy as np
import matplotlib.pyplot as plt
from logbin230119 import logbin
N=100000
m=[4,16,64,256]
deg_list=np.loadtxt('degree_list.txt',dtype=int)
i=0
while i < len(m):
   x,y=logbin(deg_list[i],scale=1.08,zeros=False)
   p=2*m[i]*(m[i]+1)/(x*(x+1)*(x+2))
   #plot (p_logbin/p_th) vs (k/root N)
   k_max=np.max(deg_list,axis=1)
   alpha=x/k_max[i]
   beta=y/p
   plt.loglog(alpha,beta,'--',label=f'm={m[i]}')
   i+=1
plt.legend()
plt.ylabel('log(p_logbin/p_th)')
plt.xlabel('log(k/k1)')
plt.show()
