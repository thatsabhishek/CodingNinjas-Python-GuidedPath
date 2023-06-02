# Problem Statement
# Write a program to find the factorial of a number.
# Factorial of n is:
#     n! = n*(n-1)*(n-2)*(n-3)...*1
# Output the factorial of 'n'. If it does not exist, output 'Error'.
# Sample Input 1 :
# 5
# Sample Output 1 :
# 120

n = int(input())
fact = 1

if n > 0:
    for i in range(1, n+1):
        fact *= i
    print(fact)
elif n == 0:
    print(fact)
else:
    print("Error")