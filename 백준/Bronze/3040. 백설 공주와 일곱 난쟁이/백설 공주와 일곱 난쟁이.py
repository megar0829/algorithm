import sys
nine = []
for _ in range(9):
    nine.append(int(sys.stdin.readline()))
for q in range(9):
    for w in range(q+1, 9):
        for e in range(w+1, 9):
            for r in range(e+1, 9):
                for t in range(r+1, 9):
                    for y in range(t+1, 9):
                        for u in range(y+1, 9):
                            sum_nine = nine[q] + nine[w] + nine[e] + nine[r] + nine[t] + nine[y] + nine[u]   
                            if sum_nine == 100:
                                seven = [nine[q], nine[w], nine[e], nine[r], nine[t], nine[y], nine[u]]
print(*seven, sep='\n')