# For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given string.
# The input string will remain unchanged if the given character(X) doesn't exist in the input string.

# Sample Input 1:
# aabccbaa
# a
# Sample Output 1:
# bccb


from os import *
from sys import *
from collections import *
from math import *



def removeAllOccurrencesOfChar(string,c):
    s = string
    x=''
    for i in s:
        if i != c:
            x+=i
    return x



string = input()
c = input()
output = removeAllOccurrencesOfChar(string,c)
print(output)
