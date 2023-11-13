import sys
input = sys.stdin.readline


tc = int(input())

for _ in range(tc):
    n = int(input())
    
    clothes = {}
    
    for _ in range(n):
        name, clothes_type = input().strip('\n').split()
        clothes.setdefault(clothes_type, 0)
        clothes[clothes_type] += 1
    
    result = 1
    for val in clothes.values():
        result *= (val + 1)
    
    print(result - 1)