# Problem Statement
# Write a program to find x to the power n (i.e. x^n). 
# Take x and n from the user. You need to print the answer.
# Note: For this question, you can assume that 0 raised to the power of 0 is 1
# Sample Input 1 :
#  3 4
# Sample Output 1 :
# 81

from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
x,n=input().split()
x,n=int(x),int(n)
if n==0:
    print(1)
else:
    print(x**n)