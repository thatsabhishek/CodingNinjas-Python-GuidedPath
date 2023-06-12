# Problem Statement
# For a given input string(str), find and return the total number of words present in it.
# It is assumed that two words will have only a single space in between.
# Also, there wouldn't be any leading and trailing spaces in the given input string.

# Sample Input 1: Coding Ninjas!
# Sample Output 1: 2

from os import *
from sys import *
from collections import *
from math import *


from sys import stdin

def countWords(string) :
	count = 0
	s = string.split(" ")
	for i in s:
		count+=1
	return count
    
    
#main
string = stdin.readline().strip();
count = countWords(string)

print(count)

