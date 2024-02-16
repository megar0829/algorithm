def gcd(x,y):     
    while x % y != 0:
        x, y = y, x % y
        
    return y    


a, b = map(int, input().split())
c, d = map(int, input().split())

top, bottom = (a * d) + (b * c), b * d

n = gcd(top, bottom) 

print(top // n, bottom // n)