import sys

INF = sys.maxsize

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, b = map(int, sys.stdin.readline().split())
    if b==0: #일방향
        graph[u].append([v, 0])
        graph[v].append([u, 1])
    elif b==1: #양방향
        graph[u].append([v, 0])
        graph[v].append([u, 0])

#print(graph)

dist = [[INF]*n for _ in range(n)]

# 인덱스 같은거는 0
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
    
#직접 인접한 노드계산
for i in range(1, n+1):
    for j in graph[i]:
        dist[i-1][j[0]-1] = j[1]

# 거쳐가는 노드계산
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i-1][j-1] = min(dist[i-1][j-1], dist[i-1][k-1] + dist[k-1][j-1])

'''
for d in dist:
    print(d)
'''
ans = []
k = int(sys.stdin.readline())
for _ in range(k):
    s, e = map(int, sys.stdin.readline().split())
    ans.append(dist[s-1][e-1])

for a in ans:
    print(a)
            
            
