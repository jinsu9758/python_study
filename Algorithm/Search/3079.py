# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
import sys

N, M = map(int, sys.stdin.readline().split())

time = list(int(sys.stdin.readline()) for _ in range(N))

#print(N, M, time)

left = min(time)
right = max(time) * M

while left <= right:
    total = 0 # 검사 받는 인원수

    mid = (left + right)//2

    for t in time:
        total += mid//t
    #print(total)        
    if M <= total:
        right = mid -1
    else:
        left = mid + 1
print(left)
