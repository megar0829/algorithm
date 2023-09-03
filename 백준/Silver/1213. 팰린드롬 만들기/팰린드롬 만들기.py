alp = {}
text = input()
N = len(text)
for i in text:
    if i not in alp:
        alp[i] = 1
    else:
        alp[i] += 1

even = []
odd = []
for k, v in alp.items():
    if v % 2:
        if v == 1:
            odd.append((k, v))
        else:
            odd.append((k, 1))
            even.append((k, v - 1))
    else:
        even.append((k, v))

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    even.sort(key=lambda x: x[0])
    start_end = ''
    mid = ''
    if odd:
        mid += odd[0][0] * odd[0][1]
    for alpha, n in even:
        start_end += alpha * (n // 2)
    result = start_end + mid + start_end[::-1]
    print(result)