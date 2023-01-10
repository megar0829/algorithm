T = int(input()) # 테스트 케이스 수

for t in range(1, T+ 1):
    # 두 숫자를 입력받기
    a, b =list(map(int, input().split()))
    # print(a, b)
    m = a // b
    n = a % b
    print(f"#{t} {m} {n}")