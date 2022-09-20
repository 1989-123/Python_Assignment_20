"""
Write a python program to create a function and print 
a list where the values are square of numbers between 1 and 30.
"""

def f1(n):
    l1 = []
    for i in range(1, n + 1):
        l1.append(i ** 2)
    print(l1)

print()
f1(30)
print()
