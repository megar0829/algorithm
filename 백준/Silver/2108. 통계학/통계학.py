import sys
input = sys.stdin.readline
import statistics

N = int(input())
numbers = sorted([int(input()) for _ in range(N)])
mode_lst = sorted(statistics.multimode(numbers))


print(round(statistics.mean(numbers)))
print(statistics.median(numbers))

if len(mode_lst) == 1:
    print(mode_lst[0])
else:
    print(mode_lst[1])

if len(numbers) == 1:
    print(0)
else:
    print(numbers[-1] - numbers[0])