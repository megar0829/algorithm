import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


N  = int(input())

def is_prime(number):
     for n in range(2, int(number ** 0.5) + 1):
          if number % n == 0:
               return False
     return True

result = []


def dfs(idx, num):
     if idx == N:
          if is_prime(int(num)):
               result.append(int(num))
          return

     if num and not is_prime(int(num)):
          return

     for n in [1, 2, 3, 5, 7, 9]:
          if not idx and n == 1:
               continue
          
          dfs(idx + 1, num + str(n))


dfs(0, "")

for rlt in sorted(result):
     print(rlt)