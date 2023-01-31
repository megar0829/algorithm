text = []
leg = 0
for _ in range(5):
    word = input()
    text.append(word)
    if len(word) > leg:
        leg = len(word)
rev_text = []
for i in range(leg):
    for j in range(5):
        if i > (len(text[j])-1) :
            pass
        else:
            rev_text.append(text[j][i])
print(*rev_text, sep='')