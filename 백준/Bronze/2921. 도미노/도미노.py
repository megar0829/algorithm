N = int(input())
point = 0
for i in range(1, N + 1):
    for j in range(i + 1):
        point += i + j    
print(point)