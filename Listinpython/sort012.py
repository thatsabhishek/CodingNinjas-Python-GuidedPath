# Problem Statement
# You ar egiven an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s. Write a solution to sort this array/list in a 'single scan'.
# 'Single Scan' refers to iterating over the array/list just once or to put it in other words, you will be visiting each element in the array/list just once.
# Note : You need to change in the given array/list itself. Hence, no need to return or print anything.

# Sample Input 1:
# 1
# 7
# 0 1 2 0 2 0 1
# Sample Output 1:
# 0 0 0 1 1 2 2 

from os import *
from sys import *
from collections import *
from math import *

def sort012(arr):
    #Your code goes here
    nextZero = 0
    nextTwo = (len(arr) - 1)
    i = 0
    while i <= nextTwo:
        if arr[i] == 0:
            arr[nextZero], arr[i] = arr[i], arr[nextZero]
            i += 1
            nextZero += 1

        elif arr[i] == 2:
            arr[nextTwo], arr[i] = arr[i], arr[nextTwo]
            nextTwo -= 1
    
        else:
            i += 1


#Driver's code
t = int(input())

while t > 0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    sort012(arr)
    print(*arr)
    
    t -= 1
