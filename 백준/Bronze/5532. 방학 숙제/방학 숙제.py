import sys
input = sys.stdin.readline

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
cnt_math = 0
cnt_word = 0
if A % C == 0:
    cnt_math = A // C
else:
    cnt_math = (A // C) + 1
if B % D == 0:
    cnt_word = B // D
else:
    cnt_word = (B // D) + 1

if cnt_math >= cnt_word:
    print(L - cnt_math)
else:
    print(L - cnt_word)