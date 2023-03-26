from collections import deque
N = int(input())
if N == 1:
    print(1)
else:
    cards = deque(list(range(1, N+1)))
    while True:
        cards.popleft()
        cards.append(cards.popleft())
        if (len(cards)) == 1:
            break
    print(cards.popleft())