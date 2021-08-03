# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

def wycinanie_stringa (str):
    str = 'Python'
    końcówka = str [-2:]
    return końcówka * 4

print (wycinanie_stringa (str))
