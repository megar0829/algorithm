import sys
input = sys.stdin.readline

a, b, c, d, e, f = list(map(int ,input().split()))

def cramer(num1, num2, num3, num4):
    result = (num1 * num4) - (num2 * num3)
    return result


x = int(cramer(c, b, f, e) / cramer(a, b, d, e))
y = int(cramer(a, c, d, f) / cramer(a, b, d, e))
print(x, y)