import sys
import heapq

INF = sys.maxsize

#출발지 -> 목적지
def dijkstra(start_node):
    distance = [INF] * (N+1)
    queue = []
    distance[start_node] = 0
    heapq.heappush(queue, [distance[start_node], start_node])

    while queue:
        cur_distance, cur_node = heapq.heappop(queue)
        if cur_distance > distance[cur_node]:
            continue
        for nx_node, nx_distance in graph[cur_node]:
            gap_distance = cur_distance + nx_distance
            if gap_distance < distance[nx_node]:
                distance[nx_node] = gap_distance
                heapq.heappush(queue, [gap_distance, nx_node])
    return distance[X]

#목적지 -> 출발지
def dijkstra2(start_node, i):
    distance = [INF] * (N+1)
    queue = []
    distance[start_node] = 0
    heapq.heappush(queue, [distance[start_node], start_node])

    while queue:
        cur_distance, cur_node = heapq.heappop(queue)
        if cur_distance > distance[cur_node]:
            continue
        for nx_node, nx_distance in graph[cur_node]:
            gap_distance = cur_distance + nx_distance
            if gap_distance < distance[nx_node]:
                distance[nx_node] = gap_distance
                heapq.heappush(queue, [gap_distance, nx_node])
    return distance[i]


N, M, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    node, link_node, weight = map(int, sys.stdin.readline().split())
    graph[node].append([link_node, weight])

#print(graph)

result = []
for i in range(1, N+1):
    result.append(dijkstra(i) + dijkstra2(X, i))


print(max(result))
