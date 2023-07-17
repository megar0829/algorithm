N = int(input())
leave_apples = 0
for _ in range(N):
    students, apples = map(int, input().split())
    leave_apples += apples % students
print(leave_apples)
    