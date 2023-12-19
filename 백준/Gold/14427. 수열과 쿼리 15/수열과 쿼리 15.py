import sys
input = sys.stdin.readline

# Segment-Tree 생성
def create_seg(node, start, end):
    # node == leaf node 일 경우
    if start == end:
        tree[node] = (arr[start], start)
    
    # node != leaf node
    else:
        create_seg(node * 2, start, (start + end) // 2)
        create_seg((node * 2) + 1, ((start + end) // 2) + 1, end)
        
        if tree[node * 2][0] > tree[(node * 2) + 1][0]:
            less_idx = (node * 2) + 1
        else:
            less_idx = node * 2
        
        tree[node] = (tree[less_idx][0], tree[less_idx][1])    
    
    
# Segment-Tree data 수정
def update_seg(node, start, end, idx, val):
    # 재귀를 통해 범위를 벗어난 경우 종료 (종료 조건)
    if idx < start or end < idx:
        return
    
    if start == end:
        tree[node] = (val, start)
        return
    
    update_seg(node * 2, start, (start + end) // 2, idx, val)
    update_seg((node * 2) + 1, ((start + end) // 2) + 1, end, idx, val)
    
    if tree[node * 2][0] > tree[(node * 2) + 1][0]:
        less_idx = (node * 2) + 1
    else:
        less_idx = node * 2
    
    tree[node] = (tree[less_idx][0], tree[less_idx][1])  


N = int(input())
arr = [0] + list(map(int, input().split()))

tree = [(0, 0)] * (4 * N)

create_seg(1, 1, N)

M = int(input())
for _ in range(M):
    query = list(map(int, input().split()))
    
    # Ai를 v로 바꾼다
    if query[0] == 1:
        i, v = query[1], query[2]
        update_seg(1, 1, N, i, v)        
    
    # 수열에서 크기가 가장 작은 값의 인덱스를 출력
    elif query[0] == 2:
        print(tree[1][1])