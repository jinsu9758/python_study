import sys
import heapq

INF = sys.maxsize


def bfs(start_x, start_y):
    distance = [[INF] * N for _ in range(M)]
    #print(distance)
    queue = []
    distance[start_x][start_y] = 0
    heapq.heappush(queue, [distance[start_x][start_y], (start_x, start_y)])

    while queue:
        cur_distance, pos = heapq.heappop(queue)
        cur_x, cur_y = pos
        
        if cur_distance > distance[cur_x][cur_y]:
            continue

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if (0<=nx<=M-1 and 0<=ny<=N-1):
                if maps[nx][ny] == 1:
                    weight = 1
                elif maps[nx][ny] == 0:
                    weight = 0
                gap_distance = cur_distance + weight
                if gap_distance < distance[nx][ny]:
                    distance[nx][ny] = gap_distance
                    heapq.heappush(queue, [gap_distance, (nx, ny)])
    return distance[M-1][N-1]




N, M = map(int, sys.stdin.readline().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  #상 하 좌 우

maps = []
for _ in range(M):
    line = list(map(int, sys.stdin.readline().strip()))
    maps.append(line)
#print(maps)

print(bfs(0, 0))
