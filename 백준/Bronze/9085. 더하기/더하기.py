T = int(input())
for i in range(T):
    N = int(input())
    sum_num = []
    sum_num = list(map(int, input().split()))
    print(sum(sum_num))