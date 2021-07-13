# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string

def zamiana (sample_string):
    substring = sample_string.find ('not')
    substring2 = sample_string.find ('poor')
    if substring2 > substring and substring > 0 and substring2 > 0:
        sample_string = sample_string.replace (sample_string [substring: (substring2+4)], 'good')
        return sample_string
print (zamiana ('The lyrics is not that poor!'))




