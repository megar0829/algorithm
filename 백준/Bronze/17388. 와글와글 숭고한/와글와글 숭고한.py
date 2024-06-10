S, K, H = map(int, input().split())

if (S + K + H) >= 100:
    print("OK")
else:
    ans = ""
    
    if min(S, K, H) == S:
        ans = "Soongsil"
    elif min(S, K, H) == K:
        ans = "Korea"
    else:
        ans = "Hanyang"
    
    print(ans)