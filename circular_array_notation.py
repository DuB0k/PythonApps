'''
John Watson performs an operation called a right circular rotation on an array
of integers, [A0, A1, ...An-1]. After performing one right circular rotation operation,
the array is transformed from [A0, A1,...An-1] to [An-1, A0,..., An-2].

Watson performs this operation K times. To test Sherlock's ability to identify
the current element at a particular position in the rotated array, Watson asks q queries,
where each query consists of a single integer, m, for which you must print the element
at index in the rotated array (i.e., the value of Am).

Input Format
    The first line contains space-separated integers, n, k, and q, respectively.
    The second line contains space-separated integers i, where each integer describes 
    array element (where ).
    Each of the subsequent lines contains a single integer denoting .
'''
#!/bin/python3
import sys

def rotateNtimes(arr, n):
    for i in range(n):
        lastItem = arr.pop()
        arr.insert(0,lastItem)
        #print(arr)
    return arr

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

a = rotateNtimes(a,k)

for a0 in range(q):
    m = int(input().strip())
    print(a[m])
