line = sorted(list(map(int, input().split())))
print(line[0] + line[1] + min(line[2], line[0] + line[1] - 1))