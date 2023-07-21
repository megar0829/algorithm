N = int(input())
N_fact = 1
for i in range(1, N + 1):
    N_fact *= i
week = N_fact // (7 * 24 * 60 * 60)
print(week)