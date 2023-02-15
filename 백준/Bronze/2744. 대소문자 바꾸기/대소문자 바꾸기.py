word = input()
rev_word = ''
for i in word:
    if i.isupper() == True:
        rev_word += i.lower()
    else:
        rev_word += i.upper()
print(rev_word)