# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:46:49 2020

@author: Ching Hoe Lee
"""

class init_graph:
   def __init__(self,N_init):
      self.N_init=N_init
      self.attach=[]
      
   def complete(self):
      for i in range(0,self.N_init):
         for j in range(0,self.N_init-1):
            self.attach.append(i) 
      return self.attach
