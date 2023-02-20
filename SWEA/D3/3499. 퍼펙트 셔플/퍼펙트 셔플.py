T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(map(str, input().split()))
    shuffle = []
    if N % 2 == 0:
        for i in range(N//2):
            shuffle.append(cards[i])
            shuffle.append(cards[(N//2)+i])
    else:
        shuffle.append(cards[0])
        for i in range(1, (N//2)+1):
            shuffle.append(cards[(N//2)+i])
            shuffle.append(cards[i])                        
    print(f'#{t}', *shuffle)