# Problem Statement
# You are given an integer 'N'. 
# Your task is to find and return the N'th Fibonacci number using matrix exponentiation.
# Since the answer can be very large, return the answer modulo 10^9 + 7.
# Fabonacci Number is calculated using the following formula:
# F(n) = F(n-1) + F(n-2),
# where, F(1) = F(2) = 1.
# Sample Input 1:
# 2
# 10
# 7
# Sample Output 1:
# 55
# 13

from os import *
from sys import *
from collections import *
from math import *

def fibonacciNumber(n, cache={}):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    else:
        mod = 10**9+7
        cache[n] = (fibonacciNumber(n-2, cache)+fibonacciNumber(n-1, cache))%mod
        return cache[n]