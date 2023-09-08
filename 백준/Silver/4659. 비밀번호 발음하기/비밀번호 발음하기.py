vowel = 'aeiou'
while True:
    text = input()
    if text == 'end':
        break
    
    vowel_flag = False
    flag = True
    for i in range(len(text)):
        if text[i] in vowel:
            vowel_flag = True
        if i > 0:
            if text[i] == text[i - 1] and text[i] != 'e' and text[i] != 'o':
                flag = False
                break
        
        if i > 1:
            if text[i] not in vowel and text[i - 1] not in vowel and text[i - 2] not in vowel:
                flag = False
                break
            if text[i] in vowel and text[i - 1] in vowel and text[i - 2] in vowel:
                flag = False
                break
    if vowel_flag and flag:
        print('<' + text + '>', 'is acceptable.')
    else:
        print('<' + text + '>', 'is not acceptable.')