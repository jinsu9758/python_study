N, M = map(int, input().split())
lect = list(map(int, input().split()))

#print(N, M, lect)

# 우리가 구하고싶은거는 블루레이의 크기이므로, left, right를 다음과 같이 설정
left = max(lect)
right = sum(lect)

while left <= right:
    cnt = 0
    total = 0
    mid = (left + right)//2
    #print(mid)    
    for l in lect:
        total += l
        #print(total)
        if total > mid:
            cnt += 1
            total = 0
            total += l
    #print(cnt)
    if cnt < M:
        right = mid - 1
    else:
        left = mid + 1
print(left)
    
