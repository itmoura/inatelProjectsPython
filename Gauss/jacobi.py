from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A,b, N, x, info=True):
    if x is None:
        x = zeros(len(A[0]))

    D = diag(A)
    R = A - diagflat(D)

    for i in range(N):
        x = (b - dot(R,x))/D
        if info:
            pprint(x)
    return x

A = array([[10.0, -2.0, 1.0], [1.0, 5.0, 1.0], [2.0, 3.0, 10.0]])
b = array([14.0, 11.0, 8.0])
guess = array([1.0,2.0,2.0])

sol = jacobi(A, b, 25, guess)
print("A: ", A)
print("b: ", b)
print("x: ", sol)
