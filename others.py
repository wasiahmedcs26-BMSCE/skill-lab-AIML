import numpy as np
#matrix operations

A=np.array([
    [1,5,10],
    [3,7,11],
    [15,12,19]
])
B=np.array([
    [7,8,6],
    [4,8,15],
    [7,2,6]
])
print("matrix A")
print(A)
print("matrix B")
print(B)
print("sum of matrix A and B")
print(A+B)
#linalg
AA=np.array([
    [1,0,1],
    [3,1,2],
    [1,2,1]
])
detA=np.linalg.det(AA)
print("Determinant of matrix A is",detA)

inverseA=np.linalg.inv(AA)
print("Inverse of matrix A is")
print(inverseA)

# adjoint (adjugate) of matrix A
adjointA = detA * inverseA
print("Adjoint of matrix A is")
print(np.rint(adjointA).astype(int))    
#solving linear equations
#2x+y=5 x+3y=6
A1=np.array([[2,1],[3,1]])
B1=np.array([5,6])
X=np.linalg.solve(A1,B1)
print("Solution of the system of equations is")
print(X)



