import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

#print(M, N)

box = []

for _ in range(N):
    tomatoes = list(map(int, sys.stdin.readline().split()))
    box.append(tomatoes)
#print(box)

visit = [[0 for _ in range(M)] for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1] #위 아래 오른쪽 왼쪽

def bfs():
    while queue:
        node = queue.popleft()
        for i in range(4):
            x2 = node[0] + dx[i]
            y2 = node[1] + dy[i]
            if (0<=x2<N and 0<=y2<M) and visit[x2][y2]==0:
                if box[x2][y2] == 0:
                    visit[x2][y2] = visit[node[0]][node[1]] + 1
                    queue.append([x2, y2])
    return visit   

queue = deque() # 핵심. queue를 바깥으로 빼면서, 토마토가 익은거 동시에 큐에 넣어줌으로써, 동시에 카운트 가능!
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j])
            visit[i][j] = 1
        elif box[i][j] == -1:
            visit[i][j] = -1

visit = bfs()

max1 = -5

'''
for v in visit:
    print(v)
'''


answer = True
for line in visit:
    if 0 in line:
        answer = False
    elif max(line) >= max1:
        max1 = max(line)

if answer:
    print(max1-1)
else:
    print(-1)
        
