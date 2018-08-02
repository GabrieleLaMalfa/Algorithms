# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:50:50 2018

@author: Gabriele
"""

import numpy as np

## Merge and CountSplitInv Algorithm ##

def split_count(a, b, c, d):
    #1.Split a into c and d
    a_split = len(a)/2
    a_split = int(a_split)
    c = a[0 : a_split]
    d = a[a_split : ]
    num_inversion = 0
    #2.Sort and count for each division
    for i in range (len(c)):
        for j in range (i + 1, len(c)):
            if c[i] >= c[j]:
                c[i], c[j] = c[j] , c[i] 
                num_inversion = num_inversion +1    
    for i in range (len(d)):
        for j in range (i + 1, len(d)):
            if d[i] >= d[j]:
                d[i], d[j] = d[j] , d[i] 
                num_inversion = num_inversion +1
    return a , c , d 
    
    #3.form the array b, sort it and count the inversions
    i = 0
    j = 0
    b = np.zeros(len(a))
 
    for k in range (len(a)):
        if c[i] < d[j]:
            b[k] = c[i]
            i = i+1
        else:
            b[k] = d[j]
            j = j+1
            num_inversion = num_inversion + 1
      
    ind_length = i+j
    while i>j:
        b[ind_length] = d[j]
        j = j+1
    while j>i:
        b[ind_length] = c[i]
        i = i+1        
                                 
        
                           
            
            
    