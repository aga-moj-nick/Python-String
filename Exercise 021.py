# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.


def zwiększanie_liter (string):
    duże_litery = 0
    for litery in string [:4]:
        if litery.upper () == litery:
            duże_litery += 1
        if duże_litery >= 2:
            return string.upper ()
        else:
            return string
    return string

print (zwiększanie_liter ("PyThon"))
print (zwiększanie_liter ("PytHon"))
print (zwiększanie_liter ("Python"))

   
