W = [int(input()) for _ in range(10)]
K = [int(input()) for _ in range(10)]
W_top = []
K_top = []
for i in range(3):
    W_top.append(max(W))
    W.pop(W.index(max(W)))
    K_top.append(max(K))
    K.pop(K.index(max(K)))
print(sum(W_top), sum(K_top))