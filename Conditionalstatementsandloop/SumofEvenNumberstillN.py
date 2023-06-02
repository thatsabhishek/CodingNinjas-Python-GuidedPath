# Problem Statement
# Given a number N, print sum of all even numbers from 1 to N.
# Sample Input :
#  6
# Sample Output :
# 12

#Your code goes here
n = int(input())
sum=0
for i in range(n+1):
    if i%2==0:
        sum+=i
print(sum)