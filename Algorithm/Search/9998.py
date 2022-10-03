# 삼분 탐색 (Tenary-Search)
# https://velog.io/@blankspxcx/%EC%82%BC%EB%B6%84-%ED%83%90%EC%83%89-Tenary-Search

import sys

N = int(sys.stdin.readline())

Y = list(map(int, sys.stdin.readline().split()))
D = list(map(int, sys.stdin.readline().split()))

L = 0
R = max([max(Y), max(D)])

def def_cnt(middle, N):
    result_cnt = [0 for _ in range(N)]
    target_list = [0 for _ in range(N)]
    
    for i in range(0, N//2+1):
        target_list[i] = N//2 - i + middle
    for i in range(N//2+1, N):
        target_list[i] = i - N//2 + middle
    for index in range(N):
        result_cnt[index] = abs(target_list[index] - Y[index])
        result_cnt[index] += abs(target_list[index] - D[index])
    return sum(result_cnt)

while L < R:
    M1 = (2*L+R)//3
    M2 = (L+2*R)//3
    
    M1_cnt = def_cnt(M1, N)
    M2_cnt = def_cnt(M2, N)
    
    if M1_cnt <= M2_cnt:
        R = M2
    elif M1_cnt > M2_cnt:
        L = M1 + 1
print(def_cnt(L, N))
