from classes import Search

L = []
num = int(input("Enter number of elements: "))

for i in range(num):
    n = input("Enter list element: ")
    L.append(n)

st = input("Enter the stirng to search: ")
L1 = Search(st,L)

print(L1.binsearch(L,st))