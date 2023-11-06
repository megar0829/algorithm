import sys
input = sys.stdin.readline
import re

T = int(input())
for _ in range(T):
    text = input().strip('\n')
    pattern = re.compile('(100+1+|01)+')
    result = pattern.fullmatch(text)

    if result:
        print('YES')
    else:
        print('NO')