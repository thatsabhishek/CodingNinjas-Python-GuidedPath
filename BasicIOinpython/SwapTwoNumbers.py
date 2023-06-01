# Problem Statement
# Take two numbers as input and swap them and print the swapped values.
# Sample Input:
# 2
# 1 2 
# 3 4
# Sample Output:
# 2 1
# 4 3

from os import *
from sys import *
from collections import *
from math import *

def swap(a, b):
    # Write your coder here.
    a, b = b, a
    return (a, b)

