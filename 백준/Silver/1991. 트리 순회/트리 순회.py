def preorder(n):
    if n:
        print(n, end='')
        preorder(ch1[idx[n]])
        preorder(ch2[idx[n]])


def inorder(n):
    if n:
        inorder(ch1[idx[n]])
        print(n, end='')
        inorder(ch2[idx[n]])


def postorder(n):
    if n:
        postorder(ch1[idx[n]])
        postorder(ch2[idx[n]])
        print(n, end='')

N = int(input())
tree = [0] * (N + 1)
ch1 = [0] * (N + 1)
ch2 = [0] * (N + 1)
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
idx = {}
for i in range(26):
    idx[alp[i]] = i + 1
for _ in range(N):
    r, c1, c2 = input().split()
    tree[idx[r]] = r
    if c1 != '.':
        ch1[idx[r]] = c1
    if c2 != '.':
        ch2[idx[r]] = c2
preorder('A')
print()
inorder('A')
print()
postorder('A')