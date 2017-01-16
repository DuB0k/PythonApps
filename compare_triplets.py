#!/bin/python3
import sys

#a0,a1,a2 = input().strip().split(' ')
#a0,a1,a2 = [int(a0),int(a1),int(a2)]
#b0,b1,b2 = input().strip().split(' ')
#b0,b1,b2 = [int(b0),int(b1),int(b2)]

'''
a0 = 2
b0 = 1
a1 = 1
b1 = 2
a2 = 3
b2 = 2
'''
scoreA = 0
scoreB = 0

#First aproach with lambda function
#Example
#f = lambda x,y: x if (x > y) else y
#print(f(2, 3)) #3
#print(f(12,3)) #12

score = lambda x,y,s: s+1 if (x > y) else s

scoreA = score(a0, b0, scoreA) + score(a1, b1, scoreA) + score(a2, b2, scoreA)
scoreB = score(b0, a0, scoreB) + score(b1, a1, scoreB) + score(b2, a2, scoreB)

print(str(scoreA) + " " + str(scoreB)) 