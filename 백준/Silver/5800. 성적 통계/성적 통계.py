K = int(input())
for X in range(1, K + 1):
    math_grade = list(map(int, input().split()))
    N = math_grade.pop(0)
    math_grade = sorted(math_grade)
    gap = math_grade[1] - math_grade[0]
    for i in range(N - 1, 0, -1):
        next_gap = math_grade[i] - math_grade[i - 1] 
        if next_gap > gap:
            gap = next_gap
    print(f'Class {X}')
    print(f'Max {max(math_grade)}, Min {min(math_grade)}, Largest gap {gap}')
