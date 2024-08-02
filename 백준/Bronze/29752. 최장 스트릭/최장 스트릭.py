N = int(input())

A = list(input().split())

result = 0
sum = 0

for i in A : 
    if i != '0' : 
        sum += 1
        result = max(result, sum)
    
    if i == '0' : 
        result = max(result, sum)
        sum = 0

print(result)