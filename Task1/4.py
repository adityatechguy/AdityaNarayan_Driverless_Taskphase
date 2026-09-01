import numpy as np

def matrix():
    A_i = int(input("Enter the number of rows of Matrix 1: "))
    A_j = int(input("Enter the number of columns of Matrix 1: "))

    A_L = []
    for i in range(A_i):
        for j in range(A_j):
            print("Enter value", i, j,": ",end = "")
            a = int(input())
            A_L.append(a)

    A_a = np.array(A_L)
    A_a1 = A_a.reshape(A_i,A_j)

    while True:
        B_i = int(input("Enter the number of rows of Matrix 2: "))
        B_j = int(input("Enter the number of columns of Matrix 2: "))
        if B_i == A_j:
            break
        else:
            print("Error! Number of rows of matrix 2 should be equal to number of columns of matrix 1. Enter again")

    B_L = []
    for i in range(B_i):
        for j in range(B_j):
            print("Enter value", i, j,": ",end = "")
            a = int(input())
            B_L.append(a)

    B_a = np.array(B_L)
    B_a1 = B_a.reshape(B_i,B_j)   
    A_B = []
    for i  in range(A_i):
        for j in range(B_j):
            AB = []
            for i1 in range(A_j):
                AB.append(A_a1[i,i1]*B_a1[i1,j])
            AB1 = sum(AB)
            A_B.append(AB1)

    A_B1 = np.array(A_B).reshape(A_i,B_j)
    print(A_B1)
    

matrix()