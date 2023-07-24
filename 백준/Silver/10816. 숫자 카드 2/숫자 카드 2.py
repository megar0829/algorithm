import sys
input = sys.stdin.readline


N = int(input())
s_card = list(map(int, input().split()))
M = int(input())
m_card = list(map(int, input().split()))
how_many_card = {}
for i in s_card:
    if i not in how_many_card:
        how_many_card[i] = 1
    else:
        how_many_card[i] += 1
        
for j in m_card:
    if j in how_many_card:
        print(how_many_card[j], end=' ')
    else:
        print(0, end=' ')