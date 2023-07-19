gandalf = [1, 2, 3, 3, 4, 10]
sauron = [1, 2, 2, 2, 3, 5, 10]
T = int(input())
for t in range(1, T + 1):
    g = list(map(int, input().split()))
    s = list(map(int, input().split()))
    total_gan = 0
    total_sau = 0
    for i in range(len(gandalf)):
        total_gan += gandalf[i] * g[i]
    for j in range(len(sauron)):
        total_sau += sauron[j] * s[j]
    if total_gan > total_sau:
        print(f'Battle {t}: Good triumphs over Evil')    
    elif total_gan == total_sau:
        print(f'Battle {t}: No victor on this battle field')    
    else:
        print(f'Battle {t}: Evil eradicates all trace of Good')
