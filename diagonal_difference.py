#!/bin/python3
'''
Given a square matrix of size NxN, calculate the absolute difference between the sums of its diagonals.
Input Format
    The first line contains a single integer, N. The next N lines denote the matrix's rows,
    with each line containing N space-separated integers describing the columns.
Output Format
    Print the absolute difference between the two sums of the matrix's diagonals as a single integer.
Sample Input
    3
    11 2 4
    4 5 6
    10 8 -12
Sample Output
    15
'''
import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
#n = 3
#a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]] 
#print(a) 

firstDiag = 0
for r in range(n):
    firstDiag = firstDiag + a[r][r]
#print(firstDiag)

secondDiag = 0
for r, c in zip(range(n-1,-1,-1), range(n)):
    #print(a[r][c])
    secondDiag = secondDiag + a[r][c]
#print(secondDiag)

print(abs(firstDiag-secondDiag))