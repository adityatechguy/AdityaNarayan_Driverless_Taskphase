from classes import Sort
L = []
num = int(input("Enter number of elements: "))

for i in range(num):
    n = input("Enter list element: ")
    L.append(n)

L1 = Sort(L)
print(L1.selection_sort())
