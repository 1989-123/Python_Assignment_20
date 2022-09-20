"""
Write a python program to create a function to find 
the Min of three numbers. 
"""

def f1(a, b, c):
   (print("Minimum number is:",a) if a < c else print("Minimum number is:",c)) if a < b else (print("Minimum number is:",b) if b < c else print("Minimum number is:",c))


print()
f1(1000, 500, 20)
print()
