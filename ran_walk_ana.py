# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 01:27:18 2020

@author: Ching Hoe Lee
"""
import numpy as np
from logbin230119 import logbin
import matplotlib.pyplot as plt
from net_project import project
degree=np.loadtxt('rw.txt',dtype=int)
for a in degree:
  x,y=logbin(a,scale=1.0,zeros=False)
  plt.loglog(x,y,'x')
plt.show()
