del_text = 'CAMBRIDGE'
text = input()
result_text = []
for i in range(len(text)):
    if text[i] not in del_text:
        result_text.append(text[i])
print(*result_text, sep='')