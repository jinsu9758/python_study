import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

MAP = []

#입력 받기
for _ in range(N):
    line = sys.stdin.readline().strip()
    MAP.append(line)

dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1] # 위 아래 오른쪽 왼쪽

#함수 짜기
def bfs(start_node):
    result = -5
    queue = deque()
    visit = [[0]*M for _ in range(N)]
    queue.append(start_node)
    visit[start_node[0]][start_node[1]] = 1
    while queue:
        node = queue.popleft()
        x = node[0]
        y = node[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<=N-1 and 0<=ny<=M-1) and visit[nx][ny] == 0:
                if MAP[nx][ny] == 'L':
                    queue.append([nx, ny])
                    visit[nx][ny] = visit[x][y] + 1
    for v in visit:
        if max(v) >= result:
            result = max(v)
    return result-1

max_hop = -5
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'L':
            cur_max_hop = bfs([i, j])
            if cur_max_hop >= max_hop:
                max_hop = cur_max_hop
print(max_hop)