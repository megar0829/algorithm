closed_bracket = {
        ')': '(',
        ']': '['
    }
while True:
    text = input()
    bracket = []
    if text == '.':
        break
    for i in text:
        if i == '(' or i == '[':
            bracket.append(i)
        elif i == ')' or i == ']':
            if len(bracket) == 0:
                print('no')
                break
            if bracket.pop() == closed_bracket[i]:
                continue
            else:
                print('no')
                break
        if i == '.' and len(bracket) == 0:
            print('yes')
        elif i == '.' and len(bracket) != 0:
            print('no')