"""
Write a python program to create a function that prints 
the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def f1(l):
    for i in l:
        if i % 2 == 0:
           print(i, end=" ")

print()
f1([1, 2, 3, 4, 5, 6, 7, 8, 9])
