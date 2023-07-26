import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    importance = deque(list(map(int, input().split())))
    cnt = 0
    while True:
        print_num = importance.popleft()
        if len(importance) == 0:
            cnt += 1
            break
        else:
            # 중요도가 높은 문서가 남아 있다면 맨 뒤로 보내기
            if  print_num < max(importance):
                importance.append(print_num)
                M -= 1
                if M < 0:
                    M = len(importance) - 1
            # 중요도가 높은 문서라면 출력 순서 + 1
            elif print_num >= max(importance):
                cnt += 1
                if M == 0:
                    break  
                M -= 1
    print(cnt)
        