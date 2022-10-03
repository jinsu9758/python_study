# 핵심 : 첫 시작 + 차이 <= 반복문 으로 조건에 만족하는 개수를 세어, C와 비교하여
# 답을 도출함.

import sys

N, C = map(int, sys.stdin.readline().split())
house = list(int(sys.stdin.readline()) for _ in range(N))
house.sort()

L = 1
R = max(house) - min(house) + 1

while L + 1 < R:
    M = (L + R)//2
    cnt = 1
    start = house[0]
    for i in range(len(house)):
        if start + M <= house[i]:
            cnt += 1
            start = house[i]
    #print(M, cnt)
    if cnt >= C:
        L = M
        
    elif cnt < C:
        R = M
print(L)
