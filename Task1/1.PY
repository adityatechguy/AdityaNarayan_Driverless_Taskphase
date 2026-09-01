a = int(input("Number of strings: "))
L = []
D = {}
for i in range(a):
    a = input("Enter a string: ")
    L.append(a)
for i in L:
    for j in i:
        if j.upper() in D.keys() or j.lower() in D.keys():
            D[j.lower()]+=1
        else:
            D[j.lower()] = 1
print(D)