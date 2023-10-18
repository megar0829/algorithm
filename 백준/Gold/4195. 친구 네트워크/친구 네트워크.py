import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def find_set(x):
    if x == parent[x]:
        return x
    
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x,y):
    x, y = find_set(x), find_set(y)

    if x == y:
        return number[x]
    
    elif x < y:
        parent[y] = x
        number[x] += number[y]
        return number[x]
        
    elif x > y:
        parent[x] = y
        number[y] += number[x]
        return number[y]

tc = int(input())

for _ in range(tc):
    parent = {} 
    number = {}

    F = int(input())

    for _ in range(F):
        f1, f2 = input().split()
        
        if f1 not in parent.keys():
            parent[f1] = f1
            number[f1] = 1
            
        if f2 not in parent.keys():
            parent[f2] = f2
            number[f2] = 1
        
        print(union(f1,f2))