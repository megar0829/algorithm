import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

"""
1. 가장 처음에 상근이는 트리의 루트에 있는 빌딩 앞에 서있다.
2. 현재 빌딩의 왼쪽 자식에 있는 빌딩에 아직 들어가지 않았다면, 왼쪽 자식으로 이동한다.
3. 현재 있는 노드가 왼쪽 자식을 가지고 있지 않거나 왼쪽 자식에 있는 빌딩을 이미 들어갔다면, 현재 노드에 있는 빌딩을 들어가고 종이에 번호를 적는다.
4. 현재 빌딩을 이미 들어갔다 온 상태이고, 오른쪽 자식을 가지고 있는 경우에는 오른쪽 자식으로 이동한다.
5. 현재 빌딩과 왼쪽, 오른쪽 자식에 있는 빌딩을 모두 방문했다면, 부모 노드로 이동한다.
"""


def prev(n):
    global idx
   
    if n > 2 ** K - 1 or ans[n - 1]:
        return
    
    if idx >= L:
        return
    
    prev(n * 2)
    
    ans[n - 1] = arr[idx]
    idx += 1
    
    prev(n * 2 + 1)


"""
        1
   2          3
 4    5     6     7
8 9 10 11 12 13 14 15
"""

K = int(input())
arr = list(map(int, input().split()))

L = len(arr)

ans = [0] * (2 ** K - 1)

idx = 0

prev(1)

for i in range(1, K + 1):
    print(*ans[2 ** (i - 1) - 1 : 2 ** i - 1])