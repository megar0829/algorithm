a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

n = [i for i in range(n0, 101)]

def f(input_n):
    global a1, a0
    return (a1 * input_n) + a0


def g(input_n):
    global c
    return c * input_n


func = True
for i in range(101 - n0):
    if f(n[i]) <= g(n[i]):
        continue
    else:
        func = False
        break
print(int(func))