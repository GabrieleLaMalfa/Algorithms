# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:21:43 2018

@author: Gabriele
"""
import numpy as np


## Karatsuba Algorithm ##

#input: two n-digit positive integers x and y
#output: the product x*y
#assumption: n is a power of 2

def karatsuba(x, y, a, b, c, d):
    x = str(x)
    y = str(y)
    i = len(x)/2
    i =int(i)
    a = x[0:i]
    b = x[i:]
    j = len(y)/2
    j =int(j)
    c = y[0:j]
    d = y[j:]
    p = a + b
    q = c + d
    ac = np.multiply(a, c)
    bd = np.multiply(b ,d)
    pq = np.multiply(p, q)
    adbc = pq - ac - bd
    
    n = np.length(x + y)    
    if n <= 2:
        result = np.product(x, y)
    else:
        result = np.product(10^(n/2) , ac) + adbc + bd
        
    return result
            
        
    