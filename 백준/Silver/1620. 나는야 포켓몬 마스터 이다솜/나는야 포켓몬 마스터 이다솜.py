import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poketmon = [input().strip() for _ in range(N)]
poketmon_alpha = {}
poketmon_digit = {}
for i in range(N):
    poketmon_alpha[poketmon[i]] = i
    poketmon_digit[i] = poketmon[i]
quiz = [input().strip() for _ in range(M)]
for i in range(M):
    if quiz[i].isdigit():
        print(poketmon_digit[int(quiz[i]) - 1])
    else:
        print(poketmon_alpha[quiz[i]] + 1)