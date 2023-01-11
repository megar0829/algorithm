# import sys
# sys.stdin = open('input.txt', 'r')

n = int(input())
print(n//1000 + (n//100)%10 + (n//10)%10 + n%10)