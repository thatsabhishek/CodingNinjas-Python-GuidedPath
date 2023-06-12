# Problem Statement
# For a given input string(str), write a function to print all the possible substrings.

# Substring : A substring is a contiguous sequence of characters within a string.
# Example: "cod" is a substring of "coding". Whereas "cdng" is not as the characters taken are not contiguous

# Sample Input 1:
# abc
# Sample Output 1:
# a 
# ab 
# abc 
# b 
# bc 
# c 

from os import *
from sys import *
from collections import *
from math import *


def printSubstrings(string) :
    for i in range(len(string)):
        for j in range(i,len(string)):
            print(string[i:j+1])          
            
            
#main
string = input();
printSubstrings(string)
