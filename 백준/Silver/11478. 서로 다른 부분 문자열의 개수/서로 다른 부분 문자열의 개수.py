text = input()
n = len(text)
arr = set()
for i in range(1, n + 1):
    for j in range(n - i + 1):
        arr.add(text[j:j + i])
print(len(arr))