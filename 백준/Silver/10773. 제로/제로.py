import sys
input = sys.stdin.readline

K = int(input())
stack_lst = []
for _ in range(K):
    n = int(input())
    if n != 0:
        stack_lst.append(n)
    else:
        stack_lst.pop()
print(sum(stack_lst))