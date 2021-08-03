# 25. Write a Python program to create a Caesar encryption

def szyfrowanie (tekst, krok):
    odszyfrowany_tekst = []
    zaszyfrowany_tekst = []
    
    alfabet_duży = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alfabet_mały = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for litery in tekst:
        if litery in alfabet_duży:
            index = alfabet_duży.index(litery)
            szyfrowanie = (index + krok) % 26
            zaszyfrowany_tekst.append(szyfrowanie)
            nowe_litery = alfabet_duży[szyfrowanie]
            odszyfrowany_tekst.append(nowe_litery)
        elif litery in alfabet_mały:
            index = alfabet_mały.index(litery)
            szyfrowanie = (index + krok) % 26
            zaszyfrowany_tekst.append(szyfrowanie)
            nowe_litery = alfabet_mały[szyfrowanie]
            odszyfrowany_tekst.append(nowe_litery)
    return odszyfrowany_tekst

kod = szyfrowanie ("ala ma kota", 2)
print (kod)
            

