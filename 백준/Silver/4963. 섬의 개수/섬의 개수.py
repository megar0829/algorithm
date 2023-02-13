while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    cnt = 0
    island = []
    island.append([0 for _ in range (w+2)])
    for i in range(1, h+1):
        island.append(list(map(int, input().split())))
        island[i].insert(0,0)
        island[i].append(0) 
    island.append([0 for _ in range (w+2)])
    for i in range(1, h+1):
        for j in range(1, w+1):
            visit = []
            if island[i][j] == 1:
                visit.append([i,j])
                for s in visit:
                    a = s[0]
                    b = s[1]
                    island[a][b] = 2
                    if island[a][b+1] == 1 and [a,b+1] not in visit:
                        visit.append([a,b+1])
                    if island[a][b-1] == 1 and [a,b-1] not in visit:
                        visit.append([a,b-1])
                    if island[a+1][b] == 1 and [a+1,b] not in visit:
                        visit.append([a+1,b])
                    if island[a+1][b+1] == 1 and [a+1,b+1] not in visit:
                        visit.append([a+1,b+1])
                    if island[a+1][b-1] == 1 and [a+1,b-1] not in visit:
                        visit.append([a+1,b-1])
                    if island[a-1][b] == 1 and [a-1,b] not in visit:
                        visit.append([a-1,b])
                    if island[a-1][b+1] == 1 and [a-1,b+1] not in visit:
                        visit.append([a-1,b+1])
                    if island[a-1][b-1] == 1 and [a-1,b-1] not in visit:
                        visit.append([a-1,b-1])
                cnt += 1
    print(cnt)