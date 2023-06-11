# Problem Statement
# Given an array with N elements, the task is to rotate the array to the left by K steps, where K is non-negative.
# Sample Input:
# 8
# 7 5 2 11 2 43 1 1
# 2
# Sample Output:
# 2 11 2 43 1 1 7 5


from os import *
from sys import *
from collections import *
from math import *

n = int(input())
arr = [int(i) for i in input().split()]
k = int(input())
temp = []
for i in range(k):
    temp.append(arr[i])
for i in range(n-k):
    arr[i] = arr[i+k]
for i in range(k):
    arr[n-k+i] = temp[i]
for i in range(len(arr)):
    print(arr[i], end=' ')