# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.


string = input ('Podaj nazwę stringu: ')

if len (string) >= 3:
    if string.endswith ('ing'):
        old = 'ing'
        new = 'ly'
        print (string.replace (old, new))
    else:
        print (string + 'ing')
else:
    print (string)       

