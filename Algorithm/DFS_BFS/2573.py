#31% 틀림
# 반례 https://www.acmicpc.net/board/view/35110

#31% 틀림

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

ice = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    ice.append(line)

#print(ice2)

visit = [[0]*M for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1] #위 아래 오른쪽 왼쪽

def bfs(x, y):
    queue.append([x, y])
    visit[x][y] = 1
    while queue:
        link_cnt = 0
        zero_cnt = 0
        node = queue.popleft()
        cur_x = node[0]
        cur_y = node[1]
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if (0<=nx<=N-1 and 0<=ny<=M-1) and ice[nx][ny]==0:
                zero_cnt += 1
        cnt_list[cur_x][cur_y] += zero_cnt

time = 0
end = 1
while True:
    end_cnt = 0
    sep_cnt = 0
    queue=deque()
    visit = [[0]*M for _ in range(N)]
    cnt_list = [[0]*M for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if ice[n][m] != 0 and visit[n][m]==0:
                bfs(n, m)
       
    for n in range(N):
        for m in range(M):
            if ice[n][m] != 0:
                ice[n][m] -= cnt_list[n][m]
                if ice[n][m] <= 0:
                    ice[n][m] = 0

    for n in range(N):
        for m in range(M):
            if end_cnt == N * M:
                end = 0
            if cnt_list[n][m] == 4:
                sep_cnt += 1
    if end == 0:
        break
    
    if sep_cnt >= 2:
        print(time)
        break
    time += 1
    
if sep_cnt < 2:
    print(0)