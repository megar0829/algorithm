def cycle(x):
    return (x % 10)*10 + ((x//10)+x%10)%10

N = int(input())
cnt = 1
save = cycle(N)
while save != N:
    save = cycle(save)
    cnt += 1
print(cnt)