"""
def MenOfPassion(A[], n):
    sum = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            sum += A[i] * A[j]
    return sum
"""
n = int(input())
result = 0
for i in range(n):
    result += i
print(result)
print(2)