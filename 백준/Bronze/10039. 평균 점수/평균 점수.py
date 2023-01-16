avr = []
for i in range(5):
    avr.append(int(input()))
    if avr[i] < 40:
        avr[i] = 40
print(int(sum(avr)/len(avr)))

