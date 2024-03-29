N, K = map(int, input().split())

arr = list(map(int, input().split()))

right = 0

save_even = 0
save_odd = 0

ans = 0

for left in range(N):
    while save_odd <= K and right < N:
        if arr[right] % 2:
            save_odd += 1
        
        else:
            save_even += 1
        
        right += 1
        
        if not left and right == N:
            ans = save_even
            break
    
    if save_odd == K + 1:
        ans = max(ans, save_even)
    
    if arr[left] % 2:
        save_odd -= 1
    else:
        save_even -= 1

print(ans)