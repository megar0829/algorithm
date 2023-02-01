N, M = map(int, input().split())
card = list(map(int, input().split()))
blackjack = set([])
for i in card:
    for j in card:
        for k in card:
            if i == j or j ==k or k == i:
                pass
            elif i == j == k:
                pass
            else:
                if i + j + k > M:
                    pass
                else:
                    blackjack.add(i + j + k)
print(max(blackjack))