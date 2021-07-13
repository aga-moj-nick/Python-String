# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string


def zamiana (a, b):
    string_a = b [0] + b [1] + a [-1]
    string_b = a [0] + a [1] + b [-1]
    return string_a + ' ' + string_b

print (zamiana ('abc', 'xyz'))
