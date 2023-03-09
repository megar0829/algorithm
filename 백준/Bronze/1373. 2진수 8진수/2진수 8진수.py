n = input()
result = ''
if n == '0':
    print(0)
else:    
    if len(n) % 3 == 0:
        cnt = 2
        save = 0
        for i in n:
            save += int(i)*(2 **cnt)
            cnt -= 1
            if cnt < 0:
                cnt = 2
                result += str(save)
                save = 0
        print(result)
    elif len(n) % 3 == 2:
        cnt = 1
        save = 0
        for j in n[0:2]:
            save += int(j)*(2 **cnt)
            cnt -= 1
        result += str(save)
        cnt = 2
        save = 0    
        for i in n[2:]:
            save += int(i)*(2 **cnt)
            cnt -= 1
            if cnt < 0:
                cnt = 2
                result += str(save)
                save = 0
        print(result)
    elif len(n) % 3 == 1:
        result += '1'
        cnt = 2
        save = 0    
        for i in n[1:]:
            save += int(i)*(2 **cnt)
            cnt -= 1
            if cnt < 0:
                cnt = 2
                result += str(save)
                save = 0
        print(result)