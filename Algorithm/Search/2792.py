N, M = map(int, input().split())
jew = [int(input()) for _ in range(M)]
jew.sort()

#print(M, N, jew)

left = 1
right = max(jew)

while left <= right:
    total = 0
    middle = (left+right)//2

    for j in jew:
        if j % middle == 0:
            total += (j//middle)
        else:
            total += (j//middle) + 1
    if total > N:#
        left = middle + 1
        
    elif total <= N:
        right = middle - 1

print(left)
