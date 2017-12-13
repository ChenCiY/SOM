# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:39:23 2017

@author: user
"""
import numpy as np
#%%
X = []
file = open('hw2pt.dat' , 'r')
while 1:    
        line = file.readline()
        if not line:
           break
        list = line.strip().split()
        for i in range(len(list)):
            list[i] = float(list[i])
        x_list = list[:2]
        X.append(np.array(x_list))
#%%
Y = []        
file = open('hw2class.dat' , 'r')
while 1:    
        line = file.readline()
        if not line:
           break
        list = line.strip().split()
        for i in range(len(list)):
            list[i] = float(list[i])
        y_list = list[:100]
        Y.append(np.array(y_list))