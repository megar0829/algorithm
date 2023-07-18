many_in = 0
on_train = 0
for _ in range(10):
    out_train, in_train = map(int, input().split())
    on_train += in_train - out_train
    if on_train > many_in:
        many_in = on_train
print(many_in)