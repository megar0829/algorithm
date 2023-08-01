def chatbot(N):
    global cnt, q1, ans1, ans2, ans3
    cnt += 1
    print(q1)
    print(ans1)
    print(ans2)
    print(ans3)
    if cnt == N:
        return closebot(cnt)
    else:
        q1 = ('_' * 4) + q1
        ans1 = ('_' * 4) + ans1
        ans2 = ('_' * 4) + ans2
        ans3 = ('_' * 4) + ans3
        return chatbot(n)

def closebot(cnt):
    global q1, end, finish
    print(('_' * 4) + q1)
    print(('_' * (4 * cnt)) + end)
    print(('_' * (4 * cnt)) + finish)


n = int(input())
cnt = 0
q1 = '"재귀함수가 뭔가요?"'
ans1 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
ans2 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
ans3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
start = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
end = '"재귀함수는 자기 자신을 호출하는 함수라네"'
finish = '라고 답변하였지.'

print(start)
chatbot(n)
for i in range(n - 1, -1, -1):
    print(('_' * (4 * i)) + finish)