# 2. Write a Python program to count the number of characters (character frequency) in a string


string = "google.com"

liczba_znaków = {}
  
for i in string:
    if i in liczba_znaków:
        liczba_znaków[i] += 1
    else:
        liczba_znaków[i] = 1
  

print ("Liczba znaków :\n "
       +  str(liczba_znaków))
