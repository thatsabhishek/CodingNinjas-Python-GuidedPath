# Problem Statement
# Write a function to print all the divisors of a number.
# Divisors are those numbers that divide Number Entirely and leaves no remainder.
# Sample Input 1 :
# 10
# Sample Output 1 :
# 1 2 5 10

from os import *
from sys import *
from collections import *
from math import *


def printDivisors(n):
    for i in range(1,n+1):
        if(n%i == 0):
            print(i, end=' ')


n = int(input())
printDivisors(n)
