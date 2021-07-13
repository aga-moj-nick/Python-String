# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.




string = 'restart'
nowy_string = string [0]

# Pierwszy sposób:
for i in string [1:]:
    if (i == string [0]):
        nowy_string += '$'
    else:
        nowy_string += i
print (nowy_string)





# Drugi sposób:
def zamiana_literki(string):
  literka = string[0]
  string = string.replace(literka, '$')
  string = literka + string[1:]
  return string
print(zamiana_literki('restart'))
