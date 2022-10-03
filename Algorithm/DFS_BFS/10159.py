# 플로이드 와샬 알고리즘 사용하기
# 이 문제의 핵심은 정점끼리의 최솟값을 구할 필요가 없다.
# 그냥 방문할 수 있는지 없는지만 구현하면됨.
# 방문하는 경우는 숫자를 집어넣어줄것이고, 못하는 경우는 INF  집어넣어 줄것임.



import sys
from collections import deque

INF = sys.maxsize

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

avail_visit = [[INF]*(N) for _ in range(N)]

# 우선 입력받은 단방향 노드를 1로 초기화 시킴.
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    avail_visit[a-1][b-1] = 1

#print(avail_visit)

# 플로이드 알고리즘 적용하기.
for k in range(1, N+1): # 거쳐가는 노드
    for i in range(1, N+1): #시작 노드
        for j in range(1, N+1): # 목적지 노드
            if i == j:
                avail_visit[i-1][j-1] = 0
            else:
                if avail_visit[i-1][j-1] < avail_visit[i-1][k-1] + avail_visit[k-1][j-1]:
                    avail_visit[i-1][j-1] = avail_visit[i-1][j-1]
                    
                elif avail_visit[i-1][j-1] > avail_visit[i-1][k-1] + avail_visit[k-1][j-1]:
                    avail_visit[i-1][j-1] = avail_visit[i-1][k-1] + avail_visit[k-1][j-1]

for n1 in range(N):
    cnt = 0
    for n2 in range(N):
        if avail_visit[n1][n2] == INF and avail_visit[n2][n1] == INF:
            cnt += 1
    print(cnt)
            
