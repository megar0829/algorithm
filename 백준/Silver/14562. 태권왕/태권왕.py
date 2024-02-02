from collections import deque
import sys
input = sys.stdin.readline

C = int(input())


def bfs():
    que = deque([(S, T, 0)])

    while que:
        now, target, cnt = que.popleft()

        if now == target:
            return cnt

        if now * 2 <= target + 3:
            que.append((now * 2, target + 3, cnt + 1))

        if now + 1 <= target:
            que.append((now + 1, target, cnt + 1))

    return


for _ in range(C):
    S, T = map(int, input().split())

    print(bfs())