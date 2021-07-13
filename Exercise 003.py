# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string


string = 'w3resource'
count = 0


for i in string:
    count += 1
nowy_string = string [0] + string [1] + string [-2] + string [-1]

print (nowy_string)
