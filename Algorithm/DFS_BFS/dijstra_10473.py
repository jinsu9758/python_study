import sys
import heapq

INF = sys.maxsize

def cal_distance(cur_x, cur_y, end_x, end_y):
    # 거리 = 좌표들 뺀 값의 제곱 합에 루트 씌운거
    distance = ((cur_x-end_x)**2 + (cur_y-end_y)**2)**0.5
    return distance
    

def dijkstra(start_node):
    time_table = [INF] * (N+2)
    queue = []
    time_table[start_node] = 0
    heapq.heappush(queue, [time_table[start_node], start_node])

    while queue:
        cur_t, cur_node = heapq.heappop(queue)

        if cur_t > time_table[cur_node]:
            continue
        
        for nx_node, nx_t in time[cur_node]:
            gap_time = cur_t + nx_t
            if gap_time < time_table[nx_node]:
                time_table[nx_node] = gap_time
                heapq.heappush(queue, [gap_time, nx_node])
    return time_table[N+1]


start_x, start_y = map(float, sys.stdin.readline().split())
dest_x, dest_y = map(float, sys.stdin.readline().split())

N = int(sys.stdin.readline())

cannon = [[start_x, start_y]]
for _ in range(N):
    can_x, can_y = list(map(float, sys.stdin.readline().split()))
    cannon.append([can_x, can_y])
cannon.append([dest_x, dest_y])    

#print(start_x, start_y, dest_x, dest_y, cannon)

# 출발지 -> 각 노드들까지의 걷기 시간 저장 (목적지 포함)
# 출발지 : index 0 / 목적지 index N+1
# 거리 = 시간 * 속도
time = [[] for _ in range(N+2)]
for n in range(1, N+1):
    time[0].append([n, cal_distance(start_x, start_y, cannon[n][0], cannon[n][1])/5])
time[0].append([N+1, cal_distance(start_x, start_y, dest_x, dest_y)/5])

#print(time)

# 대포 -> 각 정점까지의 시간 계산하기
for i in range(1, N+1):
    for j in range(N+2):
        if i!=j:
            time[i].append([j, 2+abs(cal_distance(cannon[i][0], cannon[i][1], cannon[j][0], cannon[j][1])-50)/5])

#print(time)

#다익스트라로 최소시간 구하기
print(dijkstra(0))
    
