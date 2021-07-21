# 15. Write a Python function to create the HTML string with tags around the word(s). 


def dodawanie_tagów(tag, słowo):  
    return "<%s>%s</%s>" % (tag, słowo, tag)  
print(dodawanie_tagów('i', 'Python'))  
print(dodawanie_tagów('b', 'Python Tutorial'))  
