# 입력받은 문자열과 비교하기 위한 알파벳 튜플(자료형을 사용하기 위함)
alphabet = {'A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

# 입력 데이터 수
T = int(input())

# 입력 데이터 수만큼 반복 
for _ in range(T):
  s = set(input()) # 입력받은 문자열 set으로 튜플 만들기
  a = alphabet-s # 차집합 구하기
  sum = 0 # 아스키 코드 값의 합 구하기 위한 sum 초기화
  for i in a: 
    # 등장하지 않는 알파벳의 아스키 코드 값 더하기
    sum += ord(i)
  print(sum) # 출력