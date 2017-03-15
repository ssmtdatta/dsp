# Matrix Algebra

import numpy as np 

# define matrices and vectors

A = [ [1, 2, 3],
	  [2, 7, 4] ]

B = [ [1, -1], 
      [0,  1] ]

C = [ [5, -1], 
      [9,  1],
      [6,  0] ]

D = [ [3, -2, -1],
      [1,  2,  3] ]


u = [ [6, 2, -3, 5] ]

v = [ [3, 5, -1, 4] ]

w = [ [1, 8, 0, 5] ]


A = np.array(A)
B = np.array(B)
C = np.array(C)
D = np.array(D)

u = np.array(u)
v = np.array(v)
w = np.transpose(np.array(w))

ALPHA = 6

# all matrices as a list
M = [A, B, C, D, u, v, w]
M_names = ['A', 'B', 'C', 'D', 'u', 'v', 'w']


def matrixDimension(M):
	dim_M = map(lambda x: x.shape, M)
	dim_M = list(dim_M)
	for i in range(0, len(M)):
		print("Dimension of", M_names[i], ":", dim_M[i][0],"x",dim_M[i][1], "\n" )
	



###
#Q1. Write the dimension of each matrix
matrixDimension(M)

###
#Q2. Vector operations. 
#2.1
print("2.1   u+v = ", u + v)
print("\n")
#2.2
print("2.2   u-v = ", u - v)
print("\n")
#2.3
print("2.3   alpha u = ", ALPHA*u)
print("\n")
#2.4
print("2.4   u.v = ", np.dot(u[:,0], v))
print("\n")
#2.5
print("2.5   norm of u = ", round(np.linalg.norm(u, 2), 2))
print("\n")

###
#Q3. Matrix Operations
#3.1
print("3.1   A+C is undefined because the dimensions of A and C don't match.")
print("\n")
#3.2
print("3.2   A - C_trans = ", A - np.transpose(C))
print("\n")
#3.3
print("3.3   C_trans - 3D = ", np.transpose(C)-3*D)
print("\n")
#3.4 
print("3.4   BA = ", np.matrix(B)*np.matrix(A))
print("\n")
#3.5
print("3.5   B A_trans is undefined because their dimesions are not compatible for matrix multipliction.")




