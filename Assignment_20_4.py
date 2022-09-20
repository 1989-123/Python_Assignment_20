"""
Write a python program to create a function that 
checks whether a passed string is palindrome or not.
"""

def f1(a):
    j = a[::-1]
    if a == j:
        print("String is plaindrome")
    else:
        print("String is not palindrome")

print()
f1("radart")
print()
