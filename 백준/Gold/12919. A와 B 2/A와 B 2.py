from collections import deque


def bfs(s, t):
    que = deque()
    que.append(t)
    while que:
        word = que.popleft()
        if word == s:
            return True
        if len(word) > 1:
            for k in range(2):
                if k == 0:
                    if word[-1] == 'A':
                        text = word[:-1]
                        que.append(text)
                else:
                    if word[0] == 'B':
                        text = word[::-1]
                        text = text[:-1]
                        que.append(text)
    return False


S = input()
T = input()

if bfs(S, T):
    print(1)
else:
    print(0)