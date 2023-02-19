import sys
lst = [int(sys.stdin.readline()) for _ in range(9)]
result = []
for q in range(3):
    for w in range(q+1, 4):
        for e in range(w+1, 5):
            for r in range(e+1, 6):
                for t in range(r+1, 7):
                    for y in range(t+1, 8):
                        for u in range(y+1, 9):
                            if lst[q] + lst[w] + lst[e] + lst[r] + lst[t] + lst[y] + lst[u] == 100:
                                for i in [lst[q], lst[w], lst[e], lst[r], lst[t], lst[y], lst[u]]:
                                    result.append(i)
seven = []
for j in range(7):
    seven.append(result[j])
print(*sorted(seven), sep='\n')