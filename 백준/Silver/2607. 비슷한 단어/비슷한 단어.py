from copy import deepcopy


N = int(input())
text = list(input())

result = 0
for _ in range(N - 1):
    word = list(input())
    s_text = deepcopy(text)
    if len(word) >= len(s_text):
        for i in s_text:
            if i in word:
                word.remove(i)
        if not word or len(word) == 1:
            result +=1 
    else:    
        for i in word:
            if i in s_text:
                s_text.remove(i)
        if not s_text or len(s_text) == 1:
            result +=1 
print(result)