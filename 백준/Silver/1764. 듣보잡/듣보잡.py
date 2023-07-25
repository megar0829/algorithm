import sys
input = sys.stdin.readline


N, M = map(int, input().split())
dont_listen = set(input().strip() for _ in range(N))
dont_see = set(input().strip() for _ in range(M))
dont_listen_see = dont_listen.intersection(dont_see)
print(len(dont_listen_see))
for i in sorted(dont_listen_see):
    print(i)