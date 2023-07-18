score = [int(input()) for _ in range(8)]
score_sort = sorted(score, reverse=True)
total = []
sqc = []
for i in range(5):
    total.append(score_sort[i])
    sqc.append(score.index(score_sort[i]) + 1)
sqc = sorted(sqc)
print(sum(total))
print(*sqc)