# Problem Statement
# Reverse the given string word wise. The last word in the given string should come at 1st place, 
# the last-second at 2nd place, and so on. Individual words should remain as it is.

# Sample Input 1:
# Welcome to Coding Ninjas
# Sample Output 1:
# Ninjas Coding to Welcome


def reverseStringWordWise(string):
    word = " ".join(string.split(" ")[::-1])
    return word    


string = input()
ans = reverseStringWordWise(string)
print(ans)
        
