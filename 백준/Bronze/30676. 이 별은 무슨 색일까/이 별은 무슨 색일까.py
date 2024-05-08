# 빨간색: 620nm 이상 780nm 이하
# 주황색: 590nm 이상 620nm 미만
# 노란색: 570nm 이상 590nm 미만
# 초록색: 495nm 이상 570nm 미만
# 파란색: 450nm 이상 495nm 미만
# 남색: 425nm 이상 450nm 미만
# 보라색: 380nm 이상 425nm 미만

lamb = int(input())

if lamb >= 620:
    print("Red")
    
elif lamb >= 590:
    print("Orange")
    
elif lamb >= 570:
    print("Yellow")    
    
elif lamb >= 495:
    print("Green")  
    
elif lamb >= 450:
    print("Blue")    
    
elif lamb >= 425:
    print("Indigo")  
    
elif lamb >= 380:
    print("Violet")