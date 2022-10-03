import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

cheese = []

for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    cheese.append(line)
    
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

def delete_cheese():
    for n in range(len(zero_cnt_list)):
        for m in range(len(zero_cnt_list[n])):
            if zero_cnt_list[n][m] >= 2:
                visit[n][m] = 1
                cheese[n][m] = 0

def bfs(x, y):
    global one_cnt
    one_cnt = 0
    queue = deque()
    queue.append([x, y])
    visit[x][y] = 1
    while queue:
        node = queue.popleft()
        cur_x = node[0]
        cur_y = node[1]
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if (0<=nx<=N-1 and 0<=ny<=M-1):
                if cheese[nx][ny]==0 and visit[nx][ny]==0:
                    visit[nx][ny] = 1
                    queue.append([nx, ny])
                elif cheese[nx][ny] == 1:
                    zero_cnt_list[nx][ny] += 1
                    one_cnt += 1
    delete_cheese()

    
time = 0
one_cnt = 1
while True:
    if one_cnt > 0:
        visit = [[0]*M for _ in range(N)]
        zero_cnt_list = [[0]*M for _ in range(N)]
        bfs(0, 0)
        time += 1
    elif one_cnt == 0:
        print(time - 1)
        break
    
  