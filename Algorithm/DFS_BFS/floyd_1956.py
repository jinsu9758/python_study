import sys

INF = sys.maxsize

V, E = map(int, sys.stdin.readline().split())

distance = [[INF]*V for _ in range(V)]

graph= [[] for _ in range(V+1)]

# 입력값 받기
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    
# 같은 곳으로 가는거 0으로 초기화 해주기
for i in range(V):
    for j in range(V):
        if i==j:
            distance[i][j] = 0

def floyd():
    # 직진경로 계산해주기
    for i in range(1, V+1):
        for g in graph[i]:
            distance[i-1][g[0]-1] = min(g[1] ,distance[i-1][g[0]-1])

    #각 노드 한번씩 거쳐서 계산하기
    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                distance[i-1][j-1] = min(distance[i-1][k-1] + distance[k-1][j-1], distance[i-1][j-1])

    return distance
    
dist = floyd()

_min = INF
for i in range(V):
    for j in range(V):
        if (dist[i][j] != INF and dist[j][i] != INF) and (i!=j):
            _sum = dist[i][j] + dist[j][i]
            if _min > _sum:
                _min = _sum
if _min >= INF:
    print(-1)
else:
    print(_min)
    
    
