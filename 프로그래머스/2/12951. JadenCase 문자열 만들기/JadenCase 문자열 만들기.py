def solution(s):   
    answer = ''
    
    flag = True
    for text in s:
        if flag and text != ' ':
            if text.isdigit():
                answer += text
            else:
                answer += text.upper()
            flag = False
        
        else:
            if text == ' ':
                answer += text
                flag = True
                
            else:
                answer += text.lower()
        
    return answer