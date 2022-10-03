import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
# graph[i][j][0] -> 노드 / graph[i][j][1] -> 길이

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

start, end = map(int, sys.stdin.readline().split())

'''
print(N, M)
print(start, end)
'''
#print(graph)

def bfs(start, end, M):
    queue = deque()
    visit = [0]*(N+1)
    queue.append(start)
    visit[start] = 1
    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for g in graph[node]:
            link_node, weight = g
            if visit[link_node] == 0 and weight >= M:
                queue.append(link_node)
                visit[link_node] = 1
    return False     


L = 0
R = 1000000000
while L<=R:
    M = (L + R)//2
    if bfs(start, end, M): 
        L = M+1
    else:
        R = M-1
print(R)

