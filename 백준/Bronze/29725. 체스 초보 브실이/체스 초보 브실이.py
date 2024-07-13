scoreDic = {'K' : 0, 'P' : 1, 'N' : 3, 'B' : 3, 'R' : 5, 'Q' : 9}

bSum = 0
wSum = 0

for i in range(8) : 
    board = list(map(str, input()))
    
    for name in board : 
        if name == '.' : 
            continue
        
        if name.isupper() : 
            wSum += scoreDic[name]
        else : 
            bSum += scoreDic[name.upper()]

print(wSum - bSum)