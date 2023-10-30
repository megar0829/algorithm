import sys
input = sys.stdin.readline


N, M = map(int, input().split())

password_dict = {}

for _ in range(N):
    pw, url = input().strip('\n').split()
    password_dict[pw] = url

for _ in range(M):
    search_pw = input().strip('\n')
    print(password_dict[search_pw])