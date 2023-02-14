L = int(input())
word = input()
hash_sum = 0
cnt = 0
for i in word:
    hash_sum += (ord(i) - 96) * 31**cnt
    cnt += 1
print(hash_sum)