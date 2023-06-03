# Problem Statement
# Write a program to find the total number of a primes number in a given interval.
# Given two integers S and E, count all primes between S and E.
# Sample Input 1 :
# 2 10
# Sample Output 1 :
# 4

from os import *
from sys import *
from collections import *
from math import *

def totalPrime(s,e):
    count = 0
    for i in range(s, e+1):
        prime = True
        for j in range(2,i):
            if i%j == 0:
                prime = False
                break
        if prime:
            count+=1
    return count


#Taking S and E space seperated input.
S,E = map(int,input().split(' '))
print(totalPrime(S,E))


