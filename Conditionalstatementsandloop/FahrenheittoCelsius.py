# Problem Statement
# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), 
# you need to convert all Fahrenheit values from Start to End at the gap of Winto their corresponding Celsius values and print the table.
# Note: Print the floor of the Celsius values if they are non-negative else print its ceil value.
# Sample Input:
# 0 
# 100 
# 20
# Sample Output:
# 0   -17
# 20  -6
# 40  4
# 60  15
# 80  26
# 100 37

from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
s=int(input())
e=int(input())
w=int(input())
while s<e:
    c=int(5*(s-32)/9)
    print(s,c)
    s+=w