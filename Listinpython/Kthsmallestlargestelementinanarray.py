# Problem Statement
# Given an array and a number K where K is smaller than size of array, we need to find the K’th smallest element and K'th smallest element in the given array.
# It is given that all array elements are not distinct.
# Note : If element is not present, then return -1.

# Sample Input 1:
# 1
# 3 2
# 1 2 3
# Sample Output 1:
# 2 2


from os import *
from sys import *
from collections import *
from math import *

def kthSmallestLargest(arr,k):
    arr = list(set(arr))
    r = sorted(arr)
    if len(r)<k:
        return -1, -1
    else:
        return (r[k-1], r[len(r)-k])  


#Driver's code
t = int(input())

while t > 0:
    
    n,k = map(int,input().split())
    arr = [int(i) for i in input().split()]
    small,large = kthSmallestLargest(arr,k)
    print(large,small)
    
    t -= 1
