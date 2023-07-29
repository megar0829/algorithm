L, P = map(int, input().split())
articles = list(map(int, input().split()))

for i in range(5):
    articles[i] -= L * P
print(*articles)