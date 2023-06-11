# Problem Statement
# Given an array with N elements, the task is to reverse all the aray elements and print the reversed array.
# Sample Input:
# 8
# 7 5 2 11 2 43 1 10
# Sample Output:
# 10 1 43 2 11 2 5 7

n = int(input())
arr=[int(i) for i in input().split()]
for i in range(-1, -n-1, -1):
    print(arr[i], end=' ')