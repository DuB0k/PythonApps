#!/bin/python3
'''
Consider a staircase of size N=4:
               #
              ##
             ###
            ####
Observe that its base and height are both equal to N, and the image is drawn using # symbols and spaces. 
The last line is not preceded by any spaces.
Write a program that prints a staircase of size N.
Input Format
    A single integer, , denoting the size of the staircase.
Output Format
    Print a staircase of size using # symbols and spaces.
'''
import sys

n = int(input().strip())

numSpaces = 0
numHashes = 0
step = ""

def getSpacesStr(num):
    return ' ' * num
spaces = lambda x: ' ' * x 
hashes = lambda x: '#' * x 

for i in range(1, n+1):
    numSpaces = n - i
    numHashes = i
    step = spaces(numSpaces) + hashes(numHashes)
    print(step)
    
#f = lambda x,y: x if (x > y) else y
#print(f(2, 3)) #3
#print(f(12,3)) #12