S = input()
n = len(S)
arr = [''] * n
for i in range(n):
    arr[i] = S[i:]

for i in sorted(arr):
    print(i) 