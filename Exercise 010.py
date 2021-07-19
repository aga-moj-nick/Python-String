# 10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.


def zamiana (string):
    return string[-1:] + string[1:-1] + string[:1]
   

string = "cośtam"
print (zamiana (string))



