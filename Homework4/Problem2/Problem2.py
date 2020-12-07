import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import scipy.linalg as la


matrix = np.zeros(shape=(50,50)) #defines a 50x50 matrix

for i in range(50): #iterates through columns of matrix

    for j in range(50): #iterates through rows of matrix

        if np.abs(i-j)<3: #poputates the matrix with values of 1 or 0
            matrix[i][j]=1
        else:
            matrix[i][j] = 0

eigvals, eigvecs = la.eig(matrix) #finds eigenvectors and eigenvalues
eigvals = eigvals.real # since out matrix is symmetric we can define eigenvalues as real

max = eigvals[0] #initializes the max eigenvalue
maxv = eigvecs[0] #initializes the eigenvector associated with the max eigenvalues

for k in range(1,50): #iterates through the array of eigenvalues, finding the largest one
    if eigvals[k] > max:
        max=eigvals[k]
        maxv=eigvecs[k]

print("max eigenvalue=")
print(max) #prints the max eigenvalue
print("eigenvector")
print(maxv) #prints the eigenvector associated with tthe max eigenvalue

b = np.ones(shape=(50)) #defines the vector b

for h in range(500): #power iteration
    n=b #defines b(h-1)
    b=matrix.dot(n)/np.linalg.norm(n) #updates the b vector
    if np.linalg.norm(b-n) < 10**(-6)*np.linalg.norm(b): #exits the loop and prints b when kmax is reached
        print("kmax=")
        print(h)
        print("bmax=")
        print(b)
        print("angle between b and maxv")
       
        x = b.dot(maxv)/(np.linalg.norm(b)*np.linalg.norm(maxv)) #solves for the angle between the vectors to demonstrate that the vectors are proportional
        print(np.arccos(x)) # near 0 shows that these vectors are proportional

        print("M . bmax =")
        print(matrix.dot(b)) #prints the dot product between the matrix and bmax

        print("maxeigenvalue . bmax =")
        print(b*max) #print bmax times the max eigenvalue. THis vector is in cant approx. equal to the above vector
        exit()