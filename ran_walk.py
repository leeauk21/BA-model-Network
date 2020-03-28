# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 01:18:51 2020

@author: Ching Hoe Lee
"""
import numpy as np
from logbin230119 import logbin
import matplotlib.pyplot as plt
from net_project import project
m=50
N=50000
q=[0,0.2,0.5,0.7]
random_walk_degree=[]
for k in q:
   new=project(m+1,N)
   new.random_walk(m,k)
   deg=new.degree()
   random_walk_degree.append(deg)
np.savetxt('rw.txt',random_walk_degree)
   
   