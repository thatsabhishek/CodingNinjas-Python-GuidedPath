# Aadil has been provided with a sentence in the form of a string as a function parameter. The task is to implement a function so as to print the sentence such that each word in the sentence is reversed. A word is a combination of characters without any spaces.
# Example:
# Input Sentence: "Hello, I am Aadil!"
# The expected output will print, ",olleH I ma !lidaA".

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def reverseEachWord(string) :
    ns=''
    list = string.split()
    for i in range(len(list)):
        s = list[i][::-1]
        ns = ns+s+' '
    return ns
    

#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
