N = int(input())
S = set()
for i in range(N):
    word = input()
    S.add(word)
sort_S = sorted(sorted(S),key=len)
print(*sort_S ,sep='\n')