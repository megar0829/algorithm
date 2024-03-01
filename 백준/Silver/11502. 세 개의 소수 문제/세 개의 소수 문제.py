import sys
input = sys.stdin.readline

numbers = [True] * (1001)
prime_number = []

for num in range(2, int(1000 ** 0.5) + 1):
    if numbers[num]:
        for del_num in range(num + num, 1001, num):
            numbers[del_num] = False
            
for num in range(2, 1001):
    if numbers[num]:
        prime_number.append(num)

L = len(prime_number)

T = int(input())
for _ in range(T):
    K = int(input())
    
    flag = False
    
    result = tuple()
    
    for prime_1 in prime_number:
        for prime_2 in prime_number:
            for prime_3 in prime_number:
                if prime_1 + prime_2 + prime_3 == K:
                    result = (prime_1, prime_2, prime_3)
                    break
            if result:
                break
        if result:
            break
                
    
    if result:
        print(*result)
    
    else:
        print(0)