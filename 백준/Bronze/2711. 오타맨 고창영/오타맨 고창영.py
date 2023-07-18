T = int(input())
for _ in range(T):
    num, text = input().split()
    update_text = text[:int(num) - 1] + text[int(num):]
    print(update_text)