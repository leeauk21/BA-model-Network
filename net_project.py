# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:40:36 2020

@author: Ching Hoe Lee
"""
import numpy as np
import random
from init_graph import init_graph

class project:
  
   def __init__(self,N_init,total_N):
      self.N_init=N_init
      self.total_N=total_N
      self.m=self.N_init-1
      #self.attach=[0,0,0,1,1,1,2,2,2,3,3,3]
      init = init_graph(self.N_init)
      self.attach = init.complete()
      self.node=np.arange(0,self.N_init,1)
      #for i in range(0,self.N_init):
         #for j in range(0,self.N_init-1):
            #self.attach.append(i)
  
   def pref_attach(self,m):
      for i in range(self.N_init,self.total_N):
         pool=[]
         while len(pool)< m:
            pick=random.choice(self.attach)
            if pick not in pool and pick !=i:
               self.attach.append(i)
               pool.append(pick)
               self.attach.append(pick)
               #print("pick",pick)
               #print("attach",self.attach)
               
         
   def ran_attach(self,m):
       for i in range(self.N_init,self.total_N):
         pool=[]
         while len(pool)< m:
            pick=random.choice(self.node)
            if pick not in pool and pick !=i:
               self.attach.append(i)
               pool.append(pick)
               self.attach.append(pick)
         self.node=np.append(self.node,i)
         
         
         
   def prob(self,q):
      action=['continue','stop']
      result=np.random.choice(action,p=[q,1-q])
      return result
         
   def random_walk(self,m,q):
      for i in range(self.N_init,self.total_N):
         pool=[]
         while len(pool)<m:
            v=random.choice(self.node)
            result=np.random.choice([0,1],p=[q,1-q])
            #print('initial',v)
            while result==0:
               neighbour=np.delete(self.node,v)
               v=random.choice(neighbour)
               result=np.random.choice([0,1],p=[q,1-q])
               #print('mid result',v)
               #if result==1:
                  #print('done')
                  #print('resulted v',v)
            if v not in pool and v !=i:
               #print('check',v)
               pool.append(v)
               self.attach.append(v)
               self.attach.append(i)
         self.node=np.append(self.node,i) 
         #print('pool',pool)
         
      
      
      
   def ran_walk(self,m,q):
      abcd=[0,1]
      for i in range(self.N_init,self.total_N):
         pool=[]
         while len(pool)<m:
            v=random.choice(self.node)
            result=np.random.choice(abcd,p=[q,1-q])
            while result==0:
               #v_old=v
               #print('old',v_old)
               v=random.choice(np.delete(self.node,v))
               #print('new',v)
               result=np.random.choice(abcd,p=[q,1-q])
               #if v==v_old:
                  #print('error')
                 # print('v',v)
            if v not in pool and v !=i:
               #print('result',v)
               pool.append(v)
               self.attach.append(v)
               self.attach.append(i)
         self.node=np.append(self.node,i)
            
               
            
   def pref_attach_degree_check(self):
      deg=np.unique(self.attach,return_counts=True)[1]
      for i in deg:
         if i < self.m:
            print('error')
            
            
   def cord_random_walk(self,m,q):
      for i in range(self.N_init,self.total_N):
         pick=[]
         while len(pick)<m:
            v=random.choice(self.node)
            j=0
            while j<1:
               choice=np.random.choice([0,1],p=[q,1-q])
               if choice==0:
                  neighbour=np.delete(self.node,v)
                  v=random.choice(neighbour)
               else:
                  if v not in pick and v !=i:
                     pick.append(v)
                     self.attach.append(v)
                     self.attach.append(i)
                     break
         self.node=np.append(self.node,i)
                  
               
               
      

      
               
   def degree(self):
      deg=np.unique(self.attach,return_counts=True)[1]
      return deg
      
#%%
