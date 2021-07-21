# 12. Write a Python program to count the occurrences of each word in a given sentence.


def zliczanie (str):
    stringi = str.split ()
    każde_słowo = set (stringi)
    for słowo in każde_słowo:
        print ('Osoba', słowo, 'występuje: ', stringi.count (słowo), 'razy')
    


if __name__ == "__main__":
    str = 'Ania Ania Ala Aga Beata Celina Ania Zdzisia Ala'
    zliczanie (str)


