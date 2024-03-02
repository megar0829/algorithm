N, K = map(int, input().split())

share_card = list(map(int, input().split()))
team_card = list(map(int, input().split()))

for _ in range(K):
    sum_val = -1e9
    save_val = 0
    
    for team in team_card:
        for share in share_card:
            if sum_val <= team * share:
                sum_val = team * share
                save_val = team
    
    team_card.remove(save_val)

result = -1e9
for team in team_card:
    for share in share_card:
        result = max(result, team * share)
    
print(result)