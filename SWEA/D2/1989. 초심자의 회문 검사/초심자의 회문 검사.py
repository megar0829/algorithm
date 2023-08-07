def palindrome(text):
    n = len(text)
    for i in range(n // 2):
        if text[i] != text[n - 1 - i]:
            return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc} {palindrome(input())}')