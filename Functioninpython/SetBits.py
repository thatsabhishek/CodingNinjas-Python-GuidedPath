# Problem Statement
# Write a program to count the number of 1's in the binary representation of an integer.
# Sample Input 1:
# 9
# Sample Output 1:
# 2

from os import *
from sys import *
from collections import *
from math import *

def countBits(n):
    count = 0
    while n!=0:
        bit = n%2
        if (bit == 1):
            count+=1
        n = n//2
    
    return count
  
n = int(input())
print(countBits(n))

