dish = input()
cnt = 0
height = 0
for i in dish:
    if cnt == 0:
        height += 10
        save_dish = i
        cnt += 1
    else:
        if i == save_dish:
            height += 5
            save_dish = i
        else:
            height += 10
            save_dish = i
print(height)