from classes import Coordinate

num = int(input("Enter the number of points: "))
L = []
for i in range(num):
    print("Enter x coordinate of point ", i+1,": ",end = "")
    p1 = int(input())
    print("Enter y coordinate of point ", i+1,": ",end = "")
    p2 = int(input())
    p = (p1,p2)
    L.append(p)

r1 = int(input("Enter x coordinate of reference point: "))
r2 = int(input("Enter y coordinate of reference point: "))
r = (r1,r2)

L1 = Coordinate(L,r).coordsort()
print(L1)