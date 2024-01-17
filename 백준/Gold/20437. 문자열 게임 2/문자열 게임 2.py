def check_short(a):
    global ans1, ans2
    
    save_idx = alp_dict[a][0]
    cnt = 1
    front_idx = 0
    for idx in alp_dict[a][1:]:
        cnt += 1
        
        if cnt == K:
            ans1 = min(ans1, (idx - save_idx) + 1)
            ans2 = max(ans2, (idx - save_idx) + 1)
            front_idx += 1
            save_idx = alp_dict[a][front_idx]
            cnt -= 1

    
T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    
    if K == 1:
        print(1, 1)
    
    else:
        alp_dict = dict()
        alp_set = set()
        for idx in range(len(W)):
            alp_dict.setdefault(W[idx], [])
            alp_dict[W[idx]].append(idx)
            
            alp_set.add(W[idx])
                
        alp_lst = list(alp_set)
        
        ans1 = 1e9
        ans2 = 0
        for alp in alp_lst:
            if len(alp_dict[alp]) >= K:
                check_short(alp)    
            
        if ans1 == 1e9 or not ans2:
            print(-1)
        else:
            print(ans1, ans2)