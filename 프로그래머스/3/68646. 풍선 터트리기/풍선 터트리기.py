def solution(a):
    A = len(a)
    
    visited = [0] * A
    
    left = 1e9
    right = 1e9
    
    for i in range(A):
        if a[i] < left:
            left = a[i]
            visited[i] = 1
            
        if a[(A - 1) - i] < right:
            right = a[(A - 1) - i]
            visited[(A - 1) - i] = 1
            
    return sum(visited)