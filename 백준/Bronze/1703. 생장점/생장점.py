while True:
    tree = list(map(int, input().split()))
    if len(tree) == 1:
        break
    n = tree.pop(0)
    leaf = 0
    splitting_factor = tree.pop(0)
    pruning = tree.pop(0)
    leaf += splitting_factor - pruning
    for i in range(n - 1):
        splitting_factor = tree.pop(0)
        pruning = tree.pop(0)
        leaf *= splitting_factor
        leaf -= pruning
    print(leaf)