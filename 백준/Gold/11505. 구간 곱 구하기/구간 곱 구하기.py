import sys
input = sys.stdin.readline

# Segment-Tree
# 여러 개의 데이터가 존재할 때 특정 구간의 합(최솟값, 최댓값, 곱 등)을 구하는 데 사용하는 자료구조
# 트리 종류 중에 하나로 이진 트리의 형태이며, 특정 구간의 합을 가장 빠르게 구할 수 있다는 장점이 있다. (O(logN))

# Segment-Tree 생성
def create_seg(node, start, end):
    # node == leaf node 일 경우
    # 배열의 원소 값을 반환
    if start == end:
        tree[node] = arr[start]
    
    # node != leaf node
    # 왼쪽 자식과 오른쪽 자식 트리를 만들고 곱을 저장
    else:
        tree[node] = (create_seg(node * 2, start, (start + end) // 2) * create_seg((node * 2) + 1, ((start + end) // 2) + 1, end)) % 1000000007
    
    return tree[node]
    
    
# Segment-Tree data 수정
# 배열의 원소 값을 변경하는 경우 트리 내에 해당 원소 인덱스 값이 포함된 모든 노드의 값을 변경해준다.
def update_seg(node, start, end, idx, change_val):
    # 재귀를 통해 범위를 벗어난 경우 종료 (종료 조건)
    if idx < start or idx > end:
        return
    
    # node == leaf node 일 경우
    if start == end:
        tree[node] = change_val
        return
    
    # node != leaf node 일 경우
    # 왼쪽 자식 검사
    update_seg(node * 2, start, (start + end) // 2, idx, change_val)
    # 오른쪽 자식 검사
    update_seg((node * 2) + 1, ((start + end) // 2) + 1, end, idx, change_val)

    tree[node] = (tree[node * 2] * tree[(node * 2) + 1]) % 1000000007


# segment-Tree 구간 곱 구하기
# 전체 트리에서 곱을 구하는 구간에 포함되는 노드를 모두 더한다.
# 전체 구간 start ~ end
# 곱을 구하는 구간 left ~ right
def sub_times_seg(node, start, end, left, right):
    # 구간을 벗어난 경우 0을 반환
    if left > end or right < start:
        return 1

    # 전체 구간보다 곱을 구하는 구간이 더 큰 경우
    # 전체 곱 반환
    if left <= start and end <= right:
        return tree[node]
    
    # 왼쪽 자식 노드 탐색 + 오른쪽 자식 노드 탐색
    return (sub_times_seg(node * 2, start, (start + end) // 2, left, right) * sub_times_seg((node * 2) + 1, ((start + end) // 2) + 1, end, left, right)) % 1000000007


N, M, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]

tree = [1] * (3000001)

create_seg(1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    
    # b 번째 수를 c로 바꾸기
    if a == 1:
        save_val = arr[b - 1]
        arr[b - 1] = c
        update_seg(1, 0 , N - 1, b - 1, c)
    
    # b 번째 수부터 c번째 수까지의 곱
    elif a == 2:
        print(sub_times_seg(1, 0, N - 1, b - 1, c - 1) % 1000000007)