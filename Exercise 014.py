# 14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).


sample_words = 'red, white, black, red, green, black'


words = [word for word in sample_words.split(",")]

print ((",").join(sorted(list(set(words)))))
