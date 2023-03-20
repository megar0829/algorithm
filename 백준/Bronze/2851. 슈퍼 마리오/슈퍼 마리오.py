mario = [int(input()) for _ in range(10)]
result = 0
save_sum = 0
sum = 0
for i in mario:
    sum += i
    if sum >= 100:
        result = sum
        break
    else:
        save_sum = sum
if sum == 100:
    print(sum)
elif (sum - 100) > (100 - save_sum):
    print(save_sum)
elif (sum - 100) <= (100 - save_sum):
    print(sum)