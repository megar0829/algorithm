while True:
    cnt = 0
    text = input()
    if text == '#':
        break
    for i in text:
        if i in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
            cnt += 1
    print(cnt)