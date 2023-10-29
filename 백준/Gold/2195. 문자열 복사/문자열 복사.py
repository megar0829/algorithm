fst = input()
scd = input()
rst = 0
start = 0 #문자 시작 인덱싱
end = 0 #끝 인덱싱
while True:
    if start==len(scd): #scd문자열 모두 탐색했다면
        break
    for i in range(len(fst)-(end-start)): #길이만큼의 문자열 있는지
        if fst[i:i+(end-start)+1] == scd[start:end+1]: #있다면 길이 1을 늘려서 한번더 탐색
            end+=1
            break
    else: #없다면 결과값, 문자 인덱싱 갱신
        rst+=1
        end-=1
        start = end+1
        end = start
print(rst)