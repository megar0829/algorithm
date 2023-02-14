while True:
    lst = list(map(int, input().split()))
    a = lst.pop(lst.index(min(lst)))
    b = lst.pop(lst.index(min(lst)))
    c = lst.pop()
    if a == 0 and b == 0 and c == 0:
        break
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')