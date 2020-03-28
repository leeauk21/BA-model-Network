# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:33:17 2020

@author: Ching Hoe Lee
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
class network:
   #m must be smaller than N
   def __init__(self,m,N_init):
      self.alist=[]
      self.m=m
      self.a=0
      if N_init < self.m+1:
         print("need to reset N")
      self.g=nx.complete_graph(N_init)
      
   
   def node(self):
      return list(self.g.nodes)
   def edge(self):
      return list(self.g.edges)
   
   def check(self,pick):
      check=np.unique(pick)
      if len(check)<self.m:
         return False
      elif len(check)==self.m:
         return True
      else:
         print("Error")
         #should not happen
      
   def ed_count(self):
      return len(self.edge())
   
   def add_node(self,node):
      self.g.add_node(node)
   def add_edge(self,node1,node2):
      self.g.add_edge(node1,node2)
      
   def iteration(self,N_add):
      #complete graph have m+1 node
      for i in range (len(self.node()),len(self.node())+N_add):
         self.add_node(i)
         edge_list=self.edge()
         pool=np.unique(edge_list)
         pick=np.random.choice(pool,self.m)
         while self.check(pick)==False:
            pick=np.random.choice(pool,self.m)
            self.check(pick)
         for j in pick:
            self.add_edge(i,j)
            
            
         
         
   def draw(self):
      nx.draw(self.g,with_labels=True)
      plt.draw()
   
   def degree(self):
      degree_distribution=np.unique(self.edge(),return_counts=True)
      return degree_distribution[1]
      
                
      

      
      
      
