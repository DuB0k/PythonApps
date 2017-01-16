#!/bin/python3
'''
Given an array of integers, calculate which fraction of its elements are positive, 
which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively.
Print the decimal value of each fraction on a new line
'''
import sys

#n = int(input().strip())
#arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
n = 6
arr = [-4,3,-9,0,4,1] 

numPositives = 0
numNegatives = 0
numZeroes    = 0

def countValues(value):
    '''
    This will tell Python that you don't intend to define a Var1 or Var2 variable
    inside the function's local scope. The Python interpreter sees this at module 
    load time and decides (correctly so) to look up any references to the 
    aforementioned variables in the global scope
    '''
    global numPositives, numNegatives, numZeroes
    if value > 0:
        numPositives = numPositives + 1
    elif value < 0:
        numNegatives = numNegatives + 1
    else:
        numZeroes = numZeroes + 1
    
arr = [countValues(x) for x in arr]

positivesPercent = float(numPositives / n)
negativesPercent = float(numNegatives / n)
zeroesPercent    = float(numZeroes / n)

print("%.6f" %positivesPercent)
print("%.6f" %negativesPercent)
print("%.6f" %zeroesPercent)
