import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

cheese = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    cheese.append(line)



# 가장자리(끝부분)은 무조건 0임. 가장자리를 이용해 bfs 탐색하기

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visit[x][y] = 1
    cnt = 0
    while queue:
        node = queue.popleft()
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if (0<=nx<=N-1 and 0<=ny<=M-1):
                if visit[nx][ny] == 0 and cheese[nx][ny] == 0:
                    visit[nx][ny] = 1
                    #visit_cnt[nx][ny] = 1
                    queue.append([nx, ny])
                elif visit[nx][ny] == 0 and cheese[nx][ny] == 1:
                    cheese[nx][ny] = 0
                    visit[nx][ny] = 1
                    cnt += 1
    cnt_list.append(cnt)
                

visit_cnt = [[0] * M for _ in range(N)] #1: 방문, 0: 방문x
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1] #위 아래 오른쪽 왼쪽
cnt_list = [-1]
max_hop = 0
time = 0

while True:
    visit = [[0] * M for _ in range(N)] #1: 방문, 0: 방문x
    bfs(0, 0)
    if cnt_list[-1] == 0:
        break
    time += 1  # bfs 돌때마다 시간 + 1씩 해줌.


print(time)
if cnt_list[-2]==-1:
    print(0)
else:
    print(cnt_list[-2])







'''
반례 참고

0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 1 0 0 0 1 0
0 1 0 1 0 1 0
0 1 0 0 0 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0
'''





