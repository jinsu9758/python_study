N, M = map(int, input().split())
tree_list = list(map(int, input().split()))
tree_list.sort()

left = 0
right = max(tree_list)

while left <= right:
    middle = (left+right) // 2
    tree_length = 0

    tree_length = sum(t-middle if t >= middle else 0 for t in tree_list)

    
    if tree_length >= M:
        left = middle + 1
    elif tree_length < M:
        right = middle - 1
print(right)        
