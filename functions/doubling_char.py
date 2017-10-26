#Given a string, return a string where for every char in the original, there are two chars. Eg. double_char(The) = TThhee


from __future__ import print_function    #importing print() from python 3

print("*******Doubling each characters in string*******")


def double_char(char):                   #function definition
    for i in char: print(i * 2, end = "")


char = raw_input("\nEnter the string to double its character: ")
print("\nThe resultant string is ", end = "")
double_char(char)                       #function call
