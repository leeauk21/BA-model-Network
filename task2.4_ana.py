# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:50:38 2020

@author: Ching Hoe Lee
"""
import numpy as np
import matplotlib.pyplot as plt
data=np.loadtxt('k_one.txt')
m=3
mean=[]
std=[]
c=1
N=[100,1000,10000,100000,200000,400000,600000,800000,1000000]
for i in data:
   mean.append(np.mean(i))
   std.append(np.std(i))
plt.errorbar(N,mean,yerr=std,fmt='x',label='data')
k_th=(-1+np.sqrt(1+np.multiply(4*m*(m+1)*c,N)))/2
plt.plot(N,k_th,'+',label='theoretical predictions')
plt.xlabel('N')
plt.legend()
plt.ylabel('Maximum Degree')
plt.savefig('max_degree.png')
plt.show()

