# For a given string(str), remove all the consecutive duplicate characters.
# Example:
# Input String: "aaaa"
# Expected Output: "a"

# Input String: "aabbbcc"
# Expected Output: "abc"

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def removeConsecutiveDuplicates(string) :
    s = ''
    i=0
    while i<len(string):
        x = string[i]
        j = i+1
        while j<len(string) and string[j] == x:
            j+=1
        s += string[i]
        i=j
    return s
          


#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
