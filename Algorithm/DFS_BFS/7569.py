import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

box = [[[] for _ in range(N)] for _ in range(H)]
#print(box)

for h in range(H):
    for n in range(N):
        box[h][n] = list(map(int, sys.stdin.readline().split()))
#print(box)

dz, dx, dy = [0, 0, 0, 0, -1, 1], [-1, 1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0] #위 아래 오른쪽 왼쪽 앞 뒤


def bfs():
    while queue:
        node = queue.popleft()
        for i in range(6):
            x2 = node[2] + dx[i]
            y2 = node[1] + dy[i]
            z2 = node[0] + dz[i]

            if (0<=x2<M and 0<=y2<N and 0<=z2<H) and visit[z2][y2][x2] == 0:
                if box[z2][y2][x2] == 0:
                    visit[z2][y2][x2] = visit[node[0]][node[1]][node[2]] + 1
                    queue.append([z2, y2, x2])
    return visit


visit = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
#print(visit)

queue = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            #print(box[h][n][m])
            if box[h][n][m] == 1:
                queue.append([h, n, m])
                visit[h][n][m] = 1
            elif box[h][n][m] == -1:
                visit[h][n][m] = -1
#print(queue)
#print(visit)

visit = bfs()
#print(visit)

ans = True
max1 = -5
for h in range(H):
    for n in range(N):
        #print(visit[h][n])
        if 0 in visit[h][n]:
            ans = False
            break
        else:
            if max(visit[h][n]) >= max1:
                max1 = max(visit[h][n])
                        
if ans:
    print(max1-1)
elif max1 == 1:
    print(0)
else:
    print(-1)