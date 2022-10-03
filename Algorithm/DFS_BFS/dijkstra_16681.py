import sys
import heapq

INF = sys.maxsize

def dijkstra(start_node):
    distance = [INF] * (N+1) #거리
    queue = []
    distance[start_node] = 0
    heapq.heappush(queue, [distance[start_node], start_node])
    
    while queue:
        #print(queue)
        cur_distance, cur_node = heapq.heappop(queue)

        if cur_distance > distance[cur_node]:
            continue

        for nx_node, nx_distance in spot[cur_node]:
            gap_distance = cur_distance + nx_distance
            if (gap_distance < distance[nx_node]) and (h[cur_node] < h[nx_node]):
                #print(h[cur_node], h[nx_node])
                distance[nx_node] = gap_distance
                heapq.heappush(queue, [gap_distance, nx_node])
    return distance


def calc_achieve(up_result, down_result):
    _max = (-1*INF)
    inf_cnt=0
    for i in range(1, N+1):
        if up_result[i]!=INF and down_result[i]!=INF:
            D_value = (up_result[i] + down_result[i]) * D
            E_value = h[i]*E
            final_value = E_value - D_value
            if final_value > _max:
                _max = final_value
        else :
            inf_cnt += 1
    if inf_cnt == N:
        return "Impossible"
    return _max
                
            

N, M, D, E = map(int, sys.stdin.readline().split())

h = list(map(int, sys.stdin.readline().split()))
h.insert(0, 0)
#print(h)

spot = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, weight = map(int, sys.stdin.readline().split())
    spot[a].append([b, weight])
    spot[b].append([a, weight])

#print(spot)
    
up_result = dijkstra(1)
down_result = dijkstra(N)

#print(up_result)
#print(down_result)

result = calc_achieve(up_result, down_result)
print(result)
