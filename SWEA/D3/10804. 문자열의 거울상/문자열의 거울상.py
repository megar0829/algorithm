T = int(input())
for tc in range(1, T + 1):
    text_dict = {
        'p': 'q',
        'q': 'p',
        'b': 'd',
        'd': 'b'
    }
    text = input()
    result = ''
    n = len(text)
    for i in range(n - 1, -1, -1):
        result += text_dict[text[i]]
    print(f'#{tc} {result}')