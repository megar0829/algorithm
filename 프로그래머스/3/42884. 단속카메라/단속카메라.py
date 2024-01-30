def solution(routes):
    r = len(routes)
    
    for i in range(r):
        routes[i] = (routes[i][0] + 30000, routes[i][1] + 30000)
    
    routes = sorted(routes, key=lambda x:(x[1], x[0]))
    
    answer = 0
    
    used = [False] * r
    
    for i in range(r):
        if not used[i]:
            if i == r - 1:
                answer += 1
                break
            
            used[i] = True
            answer += 1
            val = 1
            while True:
                if i + val >= r:
                    break
                
                if routes[i][1] >= routes[i + val][0]:
                    used[i + val] = True
                    val += 1            
                
                else:
                    break
    
    return answer