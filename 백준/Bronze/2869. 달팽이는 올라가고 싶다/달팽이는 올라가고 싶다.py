import math
A, B, V = list(map(int, input().split()))
rise_m = math.ceil((V - A) / (A - B)) + 1
print(int(rise_m))
