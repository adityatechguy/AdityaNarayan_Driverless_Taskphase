import csv
from classes import Coordinate
from math import *

class CSV:
    def __init__(self,):
        pass
    def csvread(self):

        rows = []
        with open('cones.csv','w',newline = '') as w:
            w1 = csv.writer(w)
            w1.writerow(['row_id','x','y','color'])
            w1.writerows([
                            [1, 2, 3, 'blue'],
                            [2, 1, 1, 'yellow'],
                            [3, 5, 4, 'blue'],
                            [4, 2, 2, 'yellow'],
                            [5, 0, 3, 'blue'],
                            [6, 4, 1, 'yellow'],
                            [7, 6, 5, 'blue'],
                            [8, 3, 3, 'yellow']
                        ])
        with open('cones.csv', 'r', newline = '') as f:
            
            reader = csv.reader(f)
            L = []
            header = next(reader)
            for row in reader:
                if not row or len(row) < 4:
                    continue

                L.append((int(row[1]),int(row[2])))
                rows.append([row[0].strip(),int(row[1]),int(row[2]),row[3].strip()])
        
        L1 = Coordinate(L,(0,0)).coordsort()
        with open('blue.csv', 'w', newline = '') as f1:
            wb = csv.writer(f1)
            wb.writerow(['cone_id','x','y'])
            for i in L1:
                for row in rows:
                    if i == (row[1],row[2]):
                        if row[3].lower() == 'blue':
                            wb.writerow([row[0],row[1],row[2]])
        with open('yellow.csv', 'w', newline = '') as f2:
            wy = csv.writer(f2)
            wy.writerow(['cone_id','x','y'])
            for i in L1:
                for row in rows:
                    if i == (row[1],row[2]):
                        if row[3].lower() == 'yellow':
                            wy.writerow([row[0],row[1],row[2]])

        blue = []
        yellow = []
        for i in rows:
            if i[3].strip().lower() == 'blue':
                blue.append(i)
            elif i[3].strip().lower() == 'yellow':
                yellow.append(i)
        yellowcoord = [(b[1], b[2]) for b in yellow]
        bluecoord = [(b[1], b[2]) for b in blue]
        with open('centreline.csv','w', newline = '') as f3:
            a = csv.writer(f3)
            a.writerow(['x','y'])
            for i in range(len(blue)):
                L = Coordinate(yellowcoord,bluecoord[i]).coordsort()
                mid = ((bluecoord[i][0]+L[0][0])/2, (bluecoord[i][1]+L[0][1])/2)
                a.writerow([mid[0],mid[1]])

A = CSV()
A.csvread()
        
        