import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())

#floor = [(i+1) for i in range(F)]
visit = [0 for _ in range(F+1)] # 0 ~ 10

def bfs(S):
    queue = deque()
    queue.append(S)
    visit[S] = 1

    while queue:
        node = queue.popleft()
        if node == G:
            return visit[node] - 1 # 맨처음 
        if (node+U) <= F and visit[(node+U)]==0:
            queue.append(node + U)
            visit[node + U] = visit[node] + 1 # 몇번째로 도는지 저장
        # elif가 아닌 if를 써줌으로써 모든 경우를 다 탐색
        if 1<=(node-D) and visit[(node-D)]==0:
            queue.append(node - D)
            visit[node - D] = visit[node] + 1
    return "use the stairs"
print(bfs(S))