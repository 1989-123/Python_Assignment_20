""" 
Write a python program to create a function that takes a 
number as a parameter and checks if the number is prime or not.
"""

def f1(n):
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime")
            break
    else:
        print("Number is prime")

print()
f1(9)
print()
