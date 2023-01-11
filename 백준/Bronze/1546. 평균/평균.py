# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
n = list(map(int, input().split()))
M = max(n)
sum = 0
for i in n:
    sum += (i / M)*100
    avr = sum/N
print(avr)