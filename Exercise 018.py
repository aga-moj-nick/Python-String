# 18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.


def trzy_pierwsze_znaki (string):
    for i in string:
        if len (string) <= 3:
            print (string)
            break
        else:
            print (string [:3])
            break
        return trzy_pierwsze_znaki (string)
        

string = 'Python'
trzy_pierwsze_znaki (string)


