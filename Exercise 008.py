# 8. Write a Python function that takes a list of words and returns the longest word and the length of the longest one.

import re

def najdłuższe_słowo (lista_słów):
    długość_słów = []
    for i in lista_słów:
        długość_słów.append ((len(i), i))
    długość_słów.sort ()
    return długość_słów[-1][1], długość_słów[-1][0]


        
        



uzytkownik = input ("Podaj trzy słowa: ")
lista_słów = re.sub ("[^\w]", " ", uzytkownik).split ()

print (lista_słów)
print (najdłuższe_słowo (lista_słów))


