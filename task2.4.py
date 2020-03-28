# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:08:45 2020

@author: Ching Hoe Lee
"""

import numpy as np
import matplotlib.pyplot as plt
from net_project import project
m=3
N=[100,1000,10000,100000,200000,400000,600000,800000,1000000]
n=5
data=[]
for i in N:
   j=0
   k_one_list=[]
   while j<n:
      new=project(m+1,i)
      new.pref_attach(m)
      k_one=np.max(new.degree())
      k_one_list.append(k_one)
      j+=1
   data.append(k_one_list)
np.savetxt('k_one.txt',data)