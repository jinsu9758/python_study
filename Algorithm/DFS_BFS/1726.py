import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

maps = []
for _ in range(M):
    line = list(map(int, sys.stdin.readline().split()))
    maps.append(line)
#print(maps)

start_x, start_y, start_dir = map(int, sys.stdin.readline().split())
end_x, end_y, end_dir = map(int, sys.stdin.readline().split())

start_x -= 1
start_y -= 1
end_x -= 1
end_y -= 1

dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0] # 동 서 남 북


def bfs(start_x, start_y, start_dir):
    queue = deque()
    queue.append([start_x, start_y, start_dir, 0])
    visit[start_x][start_y][start_dir] = 1

    while queue:
        #print(queue)
        cur_x, cur_y, cur_dir, cnt = queue.popleft()

        if cur_x == end_x and cur_y == end_y and cur_dir == end_dir:
            return cnt
        
        # 같은 방향 + 직진
        for i in range(1, 4):
            nx = cur_x + dx[cur_dir]*i
            ny = cur_y + dy[cur_dir]*i
            if (0<=nx<=M-1 and 0<=ny<=N-1) and visit[nx][ny][cur_dir]==0 and maps[nx][ny]==0:
                visit[nx][ny][cur_dir]=1
                queue.append([nx, ny, cur_dir, cnt+1])
            elif (0<=nx<=M-1 and 0<=ny<=N-1) and visit[nx][ny][cur_dir]==0 and maps[nx][ny]==1:
                break
        #다른 방향 계산
        for i in range(1, 5):
            if i != cur_dir and visit[cur_x][cur_y][i]==0:
                visit[cur_x][cur_y][i] = 1
                # 동-서 / 서-동 / 북-남 / 남-북은 두번 회전회야함.
                if (cur_dir==1 and i==2) or (cur_dir==2 and i==1) or (cur_dir==3 and i==4) or (cur_dir==4 and i==3):
                    queue.append([cur_x, cur_y, i, cnt+2])
                else:
                    queue.append([cur_x, cur_y, i, cnt+1])
                    
    

visit = [[[0]*5 for _ in range(N)]for _ in range(M)]
#print(visit)
print(bfs(start_x, start_y, start_dir))