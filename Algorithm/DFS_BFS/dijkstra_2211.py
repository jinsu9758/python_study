import sys
import heapq

INF = sys.maxsize

def dijkstra(start_node):
    distance = [INF] * (N+1)
    queue = []
    distance[start_node] = 0
    heapq.heappush(queue, [distance[start_node], start_node])

    while queue:
        cur_distance, cur_node = heapq.heappop(queue)

        if cur_distance > distance[cur_node]:
            continue

        for nx_node, nx_distance in network[cur_node]:
            gap_distance = cur_distance + nx_distance
            if gap_distance < distance[nx_node]:
                node_list.append([cur_node, nx_node])
                distance[nx_node] = gap_distance
                heapq.heappush(queue, [gap_distance, nx_node])
    return distance


N, M = map(int, sys.stdin.readline().split())

# 입력
network = [[] for _ in range(N+1)]
node_list = []
for _ in range(M):
    node, link_node, weight = map(int, sys.stdin.readline().split())
    network[node].append([link_node , weight])
    network[link_node].append([node , weight])
#print(network)

distance = dijkstra(1)

node_list.reverse()

cnt = 0
for d in distance:
    if d==INF or d==0:
        cnt += 1
print(len(distance)-cnt)

visit = [0]*(N+1)
result = []
for n in node_list:
    end_node = n[1]
    if visit[end_node] == 0:
        visit[end_node] = 1
        result.append(n)
        
#print(node_list)

for i, j in result:
    print(i, j)
