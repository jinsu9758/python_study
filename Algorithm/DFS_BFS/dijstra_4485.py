import sys
import heapq

INF = sys.maxsize

def dijkstra_bfs(start_x, start_y):
    black_coin = [[INF]*N for _ in range(N)]
    black_coin[start_x][start_y] = maps[start_x][start_y]
    queue = []
    heapq.heappush(queue, [black_coin[start_x][start_y], (start_x, start_y)])
    
    while queue:
        coin_weight, position = heapq.heappop(queue)
        cur_x, cur_y = position
        if coin_weight > black_coin[cur_x][cur_y]:
            continue
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            
            if (0<=nx<=N-1 and 0<=ny<=N-1):
                gap_coin_weight = coin_weight + maps[nx][ny]
                if gap_coin_weight < black_coin[nx][ny]:
                    black_coin[nx][ny] = gap_coin_weight
                    heapq.heappush(queue, [gap_coin_weight, (nx, ny)])
    return black_coin[N-1][N-1]


result = []
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    maps = []
    for _ in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        maps.append(line)
            
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
    
    start_x = 0
    start_y = 0
    
    cnt = dijkstra_bfs(start_x, start_y)
    result.append(cnt)
            
for r in range(len(result)):
    print("Problem {}: {}".format(r+1, result[r]))           
            
            
            