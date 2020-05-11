#!/bin/python

import sys

class Max_Heap:
    def __init__(self):
        self.root = [None]*100000
        self.size = 0

    def insert(self, value):
        point = self.size
        self.root[point] = value
        parentP = (point-1)/2
        while parentP>=0 and self.root[point] > self.root[parentP]:
            self.root[parentP], self.root[point] = self.root[point], self.root[parentP]
            point = parentP
            parentP = (point-1) / 2
        self.size += 1

    def popTop(self):
        end = self.size - 1
        top = 0
        top_value = self.root[top]
        self.root[top] , self.root[end] = self.root[end], self.root[top]
        self.size -= 1
        point = 0
        while (point+1)*2-1 <= self.size-1:
            left = (point + 1) * 2 - 1
            right = (point + 1) * 2
            if(right > self.size-1):
                next = left
            elif (self.root[left] >= self.root[right]):
                next = left
            else:
                next = right
            if self.root[point] < self.root[next]:
                self.root[point], self.root[next] = self.root[next], self.root[point]
                point = next
            else:
                break
        return top_value



class Min_Heap:
    def __init__(self):
        self.root = [None] * 100000
        self.size = 0

    def insert(self, value):
        point = self.size
        self.root[point] = value
        parentP = (point - 1) / 2
        while parentP>=0 and self.root[point] < self.root[parentP]:
            self.root[parentP], self.root[point] = self.root[point], self.root[parentP]
            point = parentP
            parentP = (point-1) / 2
        self.size += 1

    def popTop(self):
        end = self.size - 1
        top = 0
        top_value = self.root[top]
        self.root[top] , self.root[end] = self.root[end], self.root[top]
        self.size -= 1
        point = 0
        while (point+1)*2-1 <= self.size-1:
            left = (point + 1) * 2 - 1
            right = (point + 1) * 2
            if(right > self.size-1):
                next = left
            elif (self.root[left] <= self.root[right]):
                next = left
            else:
                next = right
            if self.root[point] > self.root[next]:
                self.root[point], self.root[next] = self.root[next], self.root[point]
                point = next
            else:
                break
        return top_value

maxH = Max_Heap()
minH = Min_Heap()
median = 0
n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a.append(a_t)
    current = a_t
    if a_i == 0:
        maxH.insert(current)
        median = float(current)
    elif current <= median:
        if (maxH.size - minH.size) == 1:
            temp = maxH.popTop()
            minH.insert(temp)
            maxH.insert(current)
            median = (float(maxH.root[0]) + float(minH.root[0]))/2
        elif (maxH.size - minH.size) == 0:
            maxH.insert(current)
            median = float(maxH.root[0])
        else:
            maxH.insert(current)
            median = (float(maxH.root[0]) + float(minH.root[0])) / 2
    else:
        if (maxH.size - minH.size) == -1:
            temp = minH.popTop()
            maxH.insert(temp)
            minH.insert(current)
            median = (float(maxH.root[0]) + float(minH.root[0]))/2
        elif (maxH.size - minH.size) == 0:
            minH.insert(current)
            median = float(minH.root[0])
        else:
            minH.insert(current)
            median = (float(maxH.root[0]) + float(minH.root[0])) / 2

    print "%.1f" %median

