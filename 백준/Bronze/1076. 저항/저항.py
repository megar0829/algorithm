color = {
    'black': 0, 
    'brown': 1, 
    'red': 2, 
    'orange': 3, 
    'yellow': 4, 
    'green': 5, 
    'blue': 6, 
    'violet': 7, 
    'grey': 8, 
    'white': 9
}
a = input()
b = input()
c = input()
result = ((10 * color[a]) + color[b]) * (10**color[c])
print(result)