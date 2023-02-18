import sys
N = int(sys.stdin.readline())
numbers = [0, 1]
for i in range(N-1):
    numbers.append(numbers[i] + numbers[i+1])
print(numbers[N])