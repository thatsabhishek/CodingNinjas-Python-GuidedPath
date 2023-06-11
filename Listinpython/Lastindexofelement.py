# Problem Statement
# Take an array with N elements with possibly duplicate elements as the input.
# The task is to find the index of the last occurrences of the element x in the array and, if it is not present return -1

# Sample Input 1 :
# 8
# 7 5 2 11 2 43 1 1
# 2
# Sample Output 1 :
# 4

from os import *
from sys import *
from collections import *
from math import *

n = int(input())
arr = [int(i) for i in input().split()]
x = int(input())
index = 0
for i in range(n):
    if arr[i] == x:
        index = i
if x not in arr:
    print(-1)
else:
    print(index)