"""
Write a python program to create a function that accepts 
a string and calculate the number of upper case letters and 
lower case letters. 
"""

def f1(str):
    a = 0
    b = 0
    for i in str:
        if i.isupper():
            a += 1
        elif i.islower():
            b += 1
    print("Upper letters count number is:",a)
    print("Lower letters count number is:",b)

print()
f1("JayEshvcd")
print()
