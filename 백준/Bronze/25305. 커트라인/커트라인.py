N, k = map(int, input().split())
x = list(map(int, input().split()))
print(sorted(x,reverse=True)[k-1])