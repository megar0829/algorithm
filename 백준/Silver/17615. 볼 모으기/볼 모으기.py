def move_the_ball(arr, ball):
    cnt = 0
    another_ball_cnt = 0
    
    for i in range(N):
        if arr[i] != ball:
            another_ball_cnt += 1
            
        else:
            cnt += another_ball_cnt
            another_ball_cnt = 0
    
    return cnt


N = int(input())
balls = input()

print(min(move_the_ball(balls[:], 'R'), move_the_ball(balls[:], 'B'), move_the_ball(balls[::-1], 'R'), move_the_ball(balls[::-1], 'B') ))
