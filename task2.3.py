# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:41:56 2020

@author: Ching Hoe Lee
"""

from logbin230119 import logbin
import numpy as np
import matplotlib.pyplot as plt
from net_project import project
from scipy.stats import chisquare
N=100000
m=[4,16,64,256]
degree_list=[]
for i in m:
   a=project(i+1,N)
   a.pref_attach(i)
   deg=a.degree()
   degree_list.append(deg)
np.savetxt('degree_list.txt',degree_list)
