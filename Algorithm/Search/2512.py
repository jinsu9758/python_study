N = int(input())

num = list(map(int, input().split()))
num.sort()

M = int(input())


left = 0
right = max(num)
while left <= right:
    middle = (left+right)//2
    total = 0
    for n in num:
        if n <= middle:
            total += n
        elif n > middle:
            total += middle
    if total > M:
        right=middle-1
    elif total <= M:
        left = middle+1
        
print(right)
            
            
