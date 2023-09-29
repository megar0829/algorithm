def check_palindrome(string):
    n = len(string)
    if string != string[::-1]:
        return False
    return True


S = input()
N = len(S)
for i in range(N):
    if check_palindrome(S[i:]):
        print(N + i)
        break