# Problem Statement
# Take the principal amount, rate of interest and the time period as input and calculate the simple interest.
# Note:Return answer as Floor integer value.
# Sample Input:
# 2000
# 2.2
# 4
# Sample Output:
# 176

from os import *
from sys import *
from collections import *
from math import *

p = int(input())
r = float(input())
t = int(input())
si = (p*r*t)/100
print(floor(si))