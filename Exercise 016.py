# 16. Write a Python function to insert a string in the middle of a string.


def dodawanie_do_stringa (str, słowo):
    return str [:2] + słowo + str [2:]

print (dodawanie_do_stringa ('[[]]', 'Python'))
print (dodawanie_do_stringa ('{{}}', 'PHP'))
