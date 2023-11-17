money = int(input())

arr = list(map(int, input().split()))

j = []
j_money = money
s = []
s_money = money

for i in range(14):
    while arr[i] <= j_money:
        j.append(arr[i])
        j_money -= arr[i]

for i in range(3, 14):
    if arr[i - 3] > arr[i - 2] > arr[i - 1] > arr[i]:
        if arr[i] <= s_money:
            while arr[i] <= s_money:
                s.append(arr[i])
                s_money -= arr[i]

    elif arr[i - 3] < arr[i - 2] < arr[i - 1] < arr[i]:
        for _ in range(len(s)):
            s_money += arr[i]
        s = []


for i in range(len(j)):
    j_money += arr[-1]

for i in range(len(s)):
    s_money += arr[-1]

if j_money > s_money:
    print('BNP')
elif j_money < s_money:
    print('TIMING')
else:
    print('SAMESAME')