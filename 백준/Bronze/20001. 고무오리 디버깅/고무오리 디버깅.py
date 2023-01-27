start = input()
cnt = 0
prob = ''
if start == '고무오리 디버깅 시작':
    while True:
        prob = input()
        if prob == '문제':
            cnt += 1 
        elif prob == '고무오리':
            if cnt == 0:
                cnt += 2
            else:
                cnt -= 1
        elif prob == '고무오리 디버깅 끝':
            break
if cnt <= 0:
    print('고무오리야 사랑해')
else:
    print('힝구')