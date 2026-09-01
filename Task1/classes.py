from collections import defaultdict
from math import *


class Sort:
    def __init__(self, List):
        self.List = List
    def selection_sort(self):
        for i in range(len(self.List)):
            smallest_num = i
            for j in range(i,len(self.List)):
                if self.List[j] < self.List[smallest_num]:
                    smallest_num = j
            self.List[i], self.List[smallest_num] = self.List[smallest_num], self.List[i]
        return self.List

class Search:
    def __init__(self, s, L):
        self.s = s
        self.L = Sort(L).selection_sort
        
    def binsearch(self,li,st,low = 0, high = None):
            if high ==None:
                high = len(li) - 1
            
            if high < low:
                print("Not found")
                return li
            m = (low + high) // 2
            if st == li[m]:
                print("Found")
                return li
            elif st < li[m]:
                return self.binsearch(li,st,low,m-1)
            elif st > li[m]:
                return self.binsearch(li,st,m+1,high)
            
    

class HashTable:
    def __init__(self,l):
        self.l = l

    def hash(self):
        h = [[] for i in range(10)]
        for i in self.l:
            h[i%10].append(i)
        return h

    def binsearch(self,li,st,low = 0, high = None):
        if high ==None:
            high = len(li) - 1
        
        if high < low:
            li.insert(low,st)
            return li
        m = (low + high) // 2
        if st == li[m]:
            li.insert(m,st)
            return li
        elif st < li[m]:
            return self.binsearch(li,st,low,m-1)
        elif st > li[m]:
            return self.binsearch(li,st,m+1,high)


    def hash_improved(self):
        h = [[] for i in range(10)]
        for i in self.l:
            self.binsearch(h[i%10],i)
        return h
class Coordinate:
    def __init__(self, L, P):
        self.L = L
        self.P = P
    def coordsort(self):
        D = defaultdict(list)
        for i in self.L:
            dist = sqrt(pow(i[0]-self.P[0],2)+pow(i[1]-self.P[1],2))
            D[dist].append(i)
        sorted1 = sorted(list(D.keys()))
        sorted_L= []
        for i in sorted1:
            for j in D[i]:
                sorted_L.append(j)
        return sorted_L



        