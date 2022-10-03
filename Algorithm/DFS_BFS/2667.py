import sys
from collections import deque

N = int(sys.stdin.readline())

house_list = list(sys.stdin.readline().strip() for _ in range(N))

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

visit = [[0 for _ in range(N)] for _ in range(N)]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visit[x][y] += 1
    cnt = 0
    while queue:
        node = queue.pop()
        for i in range(4):
            x2 = node[0] + dx[i]
            y2 = node[1] + dy[i]
            if(0<=x2<N and 0<=y2<N) and house_list[x2][y2] == '1' and visit[x2][y2] == 0:
                cnt += 1
                visit[x2][y2] += 1
                queue.append([x2, y2])
    return cnt

result = []

for i in range(len(house_list)):
    for j in range(len(house_list[i])):
        if house_list[i][j]=='1' and visit[i][j] == 0:
            cnt2 = 1
            cnt2 += bfs(i, j)
            if cnt2 > 0:
                result.append(cnt2)
print(len(result))
result.sort()
for r in result:
    print(r)