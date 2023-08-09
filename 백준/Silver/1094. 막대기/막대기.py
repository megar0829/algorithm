n = 64
X = int(input())
cnt = 0
result = n
while True:
    if X == result:
       cnt += 1
       break
    elif X < result:
        n //= 2
        result -= n
    else:
        n //= 2
        result += n
        cnt += 1
        if X < result:
            result -= n
            cnt -= 1
print(cnt)