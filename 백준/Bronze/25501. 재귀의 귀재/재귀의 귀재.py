length=int(input())
def isPalindrome(word, recursion):
    if len(word) <= 1:
        print(1, recursion)
    else:
        if word[0] == word[len(word)-1]:
            recursion += 1
            del word[len(word)-1]
            del word[0]
            return isPalindrome(word,recursion)
        else:
            print(0, recursion)
    

for _ in range(length):
    word=list(input())
    isPalindrome(word, 1)