import sys
input = sys.stdin.readline


N = int(input())

arr = [input().strip('\n') for _ in range(N)]

alp = dict()

for word in arr:
    word_dict = dict()
    
    for idx in range(len(word)):
        word_dict.setdefault(word[idx], [])
        word_dict[word[idx]].append(idx)
    
    index_lst = sorted(word_dict.values())
    
    save_alp = ''
    
    for i in range(len(index_lst)):
        if i != 0:
            save_alp += ","
        
        for val in index_lst[i]:
            save_alp += str(val)
    
    alp.setdefault(save_alp[:], 0)
    alp[save_alp[:]] += 1

ans = 0

for cnt in alp.values():
    ans += (cnt * (cnt - 1)) // 2

print(ans)