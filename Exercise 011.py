# 11. Write a Python program to remove the characters which have odd index values of a given string.

def usuwanie (string):
    ostateczny_string = ''
    for item in range (len (string)):
        if item % 2 == 0:
            ostateczny_string += string [item]
    return ostateczny_string

string = 'alamakota'
print (usuwanie (string))


