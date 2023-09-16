N = int(input())
load = list(map(int, input().split()))
oil = list(map(int, input().split()))
save_oil_price = oil[0]
result = save_oil_price * load[0]
for i in range(1, N - 1):
    if save_oil_price > oil[i]:
        save_oil_price = oil[i]
    result += save_oil_price * load[i]  
print(result)