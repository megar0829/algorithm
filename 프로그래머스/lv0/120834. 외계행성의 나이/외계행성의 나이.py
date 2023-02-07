def solution(age):
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g' ,'h', 'i', 'j']
    answer = ''
    for i in str(age):
        answer += alp[int(i)]    
    
    return answer