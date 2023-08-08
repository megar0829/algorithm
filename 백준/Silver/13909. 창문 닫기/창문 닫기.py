n = int(input())
arr = [i ** 2 for i in range(1, 50001)]
result = 0
for i in range(50000):
    if n < arr[i]:
        result = i
        break
print(result)