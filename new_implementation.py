# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:02:14 2020

@author: Ching Hoe Lee
"""
import networkx as nx
import numpy as np
import random as ran
class net:
   
   def __init__(self,m):
      self.m=m
      self.N_init=m+1
      #N_init=m+1
      self.attach=[]
      self.g=nx.complete_graph(self.N_init)
      self.node=list(self.g.nodes)
      self.edge=list(self.g.edges)
      for i in range(0,self.N_init):
         for j in range(0,self.m):
            self.attach.append(i)
         
      #self.node=np.linspace(0,self.N_init-1,self.N_init,endpoint=True)
      
   def add_node(self,i):
      self.node=np.append(self.node,i)
   
   def add_edge(self,node1,node2):
      self.edge.append((node1,node2))
      self.attach.append(node1)
      self.attach.append(node2)
   
      
   
   def node_list(self):
      print(self.node)
      
   def edge_list(self):
      print(self.edge)
      
   def N_node(self):
      return len(self.node)
   def N_edge(self):
      return len(self.edge)
   
   
   def iteration(self,step):
      for i in range(len(self.node),len(self.node)+step):
         self.add_node(i)
         pick=ran.sample(self.attach,self.m)
         check=np.unique(pick)
         while len(check)<self.m:
            pick=ran.sample(self.attach,self.m)
            check=np.unique(pick)
         for j in pick:
            self.add_edge(i,j)
            
   def degree(self):
      abc=np.unique(self.attach,return_counts=True)[1]
      deg=np.unique(abc,return_counts=True)
      return deg
      
   def new_iteration(self,step):
      for i in range(len(self.node),len(self.node)+step):
         self.add_node(i)
         new_pool_list=[]
         while len(new_pool_list)<self.m:
            new_node=np.random.choice(self.attach)
            if new_node not in new_pool_list:
               new_pool_list.append(new_node)
         for j in new_pool_list:
            self.add_edge(j,i)
            
   def pref_attach(self,N):
      for i in range(self.m+1,N):
         pool=[]
         while len(pool)< self.m:
            pick=np.random.choice(self.attach)
            if pick not in pool and pick !=i:
               self.attach.append(i)
               pool.append(pick)
               self.attach.append(pick)
               #print("pick",pick)
               #print("attach",self.attach)
               
         
         
              
            
            
            
      
      
   #def iteration(self,n):
    #  for i in range(self.N_init+1,n):
         
         
      
      
   

