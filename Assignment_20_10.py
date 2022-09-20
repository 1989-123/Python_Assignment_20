""" 
Write a python program to create a function to check 
whether a string is an anagram or not.
"""

def anagram(str1, str2):
    s1 = {}
    s2 = {}
    for i in str1:
        s1.setdefault(i)
    for j in str2:
        s2.setdefault(j)
    if s1 == s2:
        print("String is anagram")
    else:
        print("String is not a anagram")

print()
anagram("listenuy", "litsenuy")
print()
