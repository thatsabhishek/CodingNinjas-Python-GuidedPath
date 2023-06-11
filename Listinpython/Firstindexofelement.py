# First index of element
# Take an array with n elements with possibly duplicate elements as the input.
# The task is to find the index of the first occurrences of the element x in the array and, if it is not present return -1

# Sample Input 1 :
# 8
# 7 5 2 11 2 43 1 1
# 2
# Sample Output 1 :
# 2

n = int(input())
arr = [int(i) for i in input().split()]
x = int(input())

for a in range(n):
    if arr[a] == x:
        print(a)
        break
else:
    print(-1)