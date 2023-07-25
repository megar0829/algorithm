import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
check_lst = list(map(int, input().split()))

check_dict = {}
for key in cards:
    check_dict.setdefault(key, 0)
    check_dict[key] += 1
    

for key in check_lst:
    check_dict.setdefault(key, 0)


for check in check_lst:
    print(check_dict[check], end=' ')

