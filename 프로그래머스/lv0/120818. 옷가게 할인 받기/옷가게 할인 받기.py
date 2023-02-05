def solution(price):
    if price >= 500000:
        answer = price * 0.8
    elif 300000 <= price :
        answer = price * 0.9
    elif 100000 <= price :
        answer = price * 0.95
    else:
        answer = price
    return int(answer)