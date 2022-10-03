import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())

visit = [[0 for _ in range(N)] for _ in range(M)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1] #위, 아래, 오른쪽, 왼쪽

# 직사각형이 들어가있는 곳은 일단 미리 색칠함.
for k in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())
    c -= 1
    d -= 1

    a_c = abs(a-c)
    b_d = abs(b-d)
    
    for j in range(b_d+1):
        for i in range(a_c+1):
            #print(b+j, a+i)
            visit[b+j][a+i] += 1
        

# 색칠된 곳 출력해서 시각화 하기
'''
for v in range(len(visit)-1, -1, -1):
    print(visit[v])

'''

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visit[x][y] = -1 # 방문한 곳은 -1로 바꾼다.
    cnt = 0
    while queue:
        node = queue.pop()
        for i in range(4):
            x2 = node[0] + dx[i]
            y2 = node[1] + dy[i]
            if (0<=x2<=M-1 and 0<=y2<=N-1) and visit[x2][y2]==0:
                cnt += 1
                visit[x2][y2] = -1
                queue.append([x2, y2])
    return cnt

result = []
for i in range(M):
    for j in range(N):
        if visit[i][j] == 0:
            cnt2 = 1
            cnt2 += bfs(i, j)
            if cnt2 > 0:
                result.append(cnt2)

result.sort()
print(len(result))
print(*result)
