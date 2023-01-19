n = int(input())
emp_log = {}
for i in range(n):
    N, log = input().split()
    emp_log[N] = log
    if log == 'leave':
        emp_log.pop(N)        
print(*list(reversed(sorted(emp_log.keys()))), sep='\n')
 