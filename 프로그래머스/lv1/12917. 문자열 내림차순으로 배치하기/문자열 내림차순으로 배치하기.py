def solution(s):
    answer = ''
    word = []
    for i in s:
        word.append(i)
    word = sorted(word, reverse = True)
    for i in word:
        answer += i
    return answer