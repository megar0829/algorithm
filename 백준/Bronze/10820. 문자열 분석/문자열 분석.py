while True:
    try:
        text = input()
        s = 0
        B = 0
        n = 0
        d = 0
        for i in text:
            if i.isalpha() == True:
                if i.islower() == True:
                    s += 1
                else:
                    B += 1
            elif i.isdigit() == True:
                n += 1
            elif i.isspace() == True:
                d += 1
        print(s, B, n, d)
    except EOFError:
        break