dict_brackets = {'{': '}', '[': ']', '(': ')', '<':'>'}
for _ in range(1, 11):
    TC = int(input())
    brackets = input()
    save_brackets = []
    for i in brackets:
        if i in dict_brackets.keys():
            save_brackets.append(dict_brackets[i])
        else:
            if i not in save_brackets:
                validation = 0
                break
            else:
                save_brackets.pop(save_brackets.index(i))
                validation = 1
    print(f'#{_} {validation}')