import sys
n = int(sys.stdin.readline())
result = ''
for i in range(n//4):
    result += 'long '
result += 'int'
print(result)