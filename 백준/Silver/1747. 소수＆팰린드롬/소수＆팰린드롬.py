def isPalindrome(num):
    num_str = str(num)
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[(len(num_str) - 1) - i]:
            return False
    return True

N = int(input())

numbers = [False, False] + [True] * (1003005)

prime_number = []

for num in range(2, int(1003006 ** 0.5) + 1):
    if numbers[num]:        
        for idx in range(num + num, 1003005, num):
            numbers[idx] = False
             
for n in range(N, 1003005):
    if numbers[n]:
        prime_number.append(n)
             
for prime in prime_number:
    if isPalindrome(prime):
        print(prime)
        break