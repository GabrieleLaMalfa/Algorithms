# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:14:23 2018

@author: Gabriele
"""
import numpy as np

## Strassen divide and conquer VS straightforward method ##

# Starightforward method
#Given two matrix X and Y obtain the Z matrix which is the multyplication of 
#the previous ones
def straight (X, Y):
    rows_X = len(X)
    cols_X = len(X[0])
    rows_Y = len(Y)
    cols_Y = len(Y[0])
    
    if cols_X != rows_Y:
      print ("Cannot multiply the two matrices. Incorrect dimensions.")
        
    Z = [[0 for row in range (cols_Y)] for col in range (rows_X)]
    print (Z)
       
    for i in range (rows_X):
        for j in range (cols_Y):
            for k in range (cols_X):
                Z[i][j] += X[i][k] * Y[k][j]
    
               

#Divide and conquer: divide a matrix (nxn) into two little matrices (n/2, n/2)
def submatrix (X,Y):
    rows_X = len(X)
    cols_X = len(X[0])
    rows_halfX = int(len(X)/2)
    cols_halfX = int(len(X[0])/2)
    rows_Y = len(Y)
    cols_Y = len(Y[0])
    rows_halfY = int(len(Y)/2)
    cols_halfY = int(len(Y[0])/2)
    
    A = B = C = D = E = F = G = H = [[0 for row in range (rows_halfX)] 
                                      for col in range (cols_halfX)]
    A = np.array(A)
    B = np.array(B)
    C = np.array(C)
    D = np.array(D)
    E = np.array(E)
    F = np.array(F)
    G = np.array(G)
    H = np.array(H)
    
    #X matrix division
    if rows_X + cols_X == 2 and rows_Y + cols_Y == 2:
         Z = np.matmul(X,Y)
    else:
        for i in range (rows_halfX):
            for j in range (cols_halfX):
                A[i][j] = X[i][j]
                C[i][j] = X[i + rows_halfX][j]
                D[i][j] = X[i + rows_halfX][j + cols_halfX]
                B[i][j] = X[i][j + cols_halfX]
                    
    #Y matrix division            
    if rows_X + cols_X == 2 and rows_Y + cols_Y == 2:
         Z = np.matmul(X,Y)
    else:
        for i in range (rows_halfY):
            for j in range (cols_halfY):
                E[i][j] = Y[i][j]
                H[i][j] = Y[i + rows_halfY][j + cols_halfY]
                F[i][j] = Y[i][j + cols_halfY]
                G[i][j] = Y[i + rows_halfY][j]

    XY = [0]
    XY = np.array(XY) 
    M1 = np.matmul(A,E) + np.matmul(B,G)
    M2 = np.matmul(A,F) + np.matmul(B,H)
    M3 = np.matmul(C,E) + np.matmul(D,G)
    M4 = np.matmul(C,F) + np.matmul(D,H)          
    
#Strassen Algorithm : given as input n matrices, a new calculus for the 
#matrices multiplication
def strassen(A, B, C, D, E, F, G, H):
    token_1 = F - H
    token_2 = A + B
    token_3 = C + D
    token_4 = G - E
    token_5 = A + D
    token_6 = E + H
    token_7 = B - D
    token_8 = G + H
    token_9 = A - C
    token_10 = E + F
    P1 = np.matmul(A, token_1)
    P2 = np.matmul(token_2, H)
    P3 = np.matmul(token_3, E)
    P4 = np.matmul(D, token_4)
    P5 = np.matmul(token_5, token_6)
    P6 = np.matmul(token_7, token_8)
    P7 = np.matmul(token_9, token_10)
    
    Q1 = P5 + P4 - P2 + P6
    Q2 = P1 + P2
    Q3 = P3 + P4
    Q4 = P1 + P5 - P3 - P7
    XY = ([Q1], [Q2], [Q3], [Q4])
    

        
        
        
        
















