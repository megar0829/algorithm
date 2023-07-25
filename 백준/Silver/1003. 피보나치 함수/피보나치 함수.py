import sys
input = sys.stdin.readline

def fibonacci(n):
    global cnt_0, cnt_1
    if n == 0:
        cnt_0 += 1
        return 0
    elif n == 1:
        cnt_1 += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci_lst = [0 for _ in range(41)]    
fibonacci_lst[0] = (1, 0)
fibonacci_lst[1] = (0, 1)
for i in range(2, 41):
    fibonacci_lst[i] = (fibonacci_lst[i - 1][0] + fibonacci_lst[i - 2][0], \
                        fibonacci_lst[i - 1][1] + fibonacci_lst[i - 2][1])

T = int(input())
for _ in range(T):
    N = int(input())
    print(*fibonacci_lst[N])