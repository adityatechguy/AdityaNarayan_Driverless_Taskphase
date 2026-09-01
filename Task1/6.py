from classes import HashTable

num = int(input("Enter the number of integers: "))
L = []
for i in range(num):
    a = int(input('Enter the number: '))
    L.append(a)

A1 = HashTable(L)
b = A1.hash_improved()

for i in b:
    print(i)
    