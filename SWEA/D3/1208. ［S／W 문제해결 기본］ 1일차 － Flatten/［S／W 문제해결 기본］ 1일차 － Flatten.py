for t in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    for i in range(N):
        if max(boxes) - min(boxes) <= 1:
            break
        else:
            boxes[boxes.index(max(boxes))] -= 1
            boxes[boxes.index(min(boxes))] += 1
    print(f'#{t} {max(boxes) - min(boxes)}')
            