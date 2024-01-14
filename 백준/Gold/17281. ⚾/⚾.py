from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
players = [list(map(int, input().split())) for _ in range(N)]
player_numbers = [number for number in range(1, 9)]

result = 0
for permutation in permutations(player_numbers): 
    
    order_lst = list(permutation)
    batter_lst = order_lst[:3] + [0] + order_lst[3:] 
    
    num, score = 0, 0 
    for player_results in players: 
        out_count = 0
        base_1st, base_2nd, base_3rd = 0, 0, 0 
        
        while out_count < 3: 
            # 아웃
            if player_results[batter_lst[num]] == 0:
                out_count += 1 
            
            # 안타 : 1루씩 진루
            elif player_results[batter_lst[num]] == 1: 
                score += base_3rd 
                base_1st, base_2nd, base_3rd = 1, base_1st, base_2nd
            
            # 2루타 : 2루씩 진루
            elif player_results[batter_lst[num]] == 2: 
                score += base_2nd + base_3rd 
                base_1st, base_2nd, base_3rd = 0, 1, base_1st
                
            # 3루타 : 3루씩 진루
            elif player_results[batter_lst[num]] == 3:
                score += base_1st + base_2nd + base_3rd
                base_1st, base_2nd, base_3rd = 0, 0, 1
            
            # 홈런 : 모두 홈으로
            elif player_results[batter_lst[num]] == 4:
                score += base_1st + base_2nd + base_3rd + 1
                base_1st, base_2nd, base_3rd = 0, 0, 0
                
            num = (num + 1) % 9

    result = max(result, score)
    
print(result)