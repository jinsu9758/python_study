#다익스트라 예제문제 -3 < 백준 1504 >

import heapq
import sys

INF = sys.maxsize

def dijkstra(start_node):
    distance = [INF] * (N+1)
    queue = []
    distance[start_node] = 0
    #print(distance)    
    heapq.heappush(queue, (distance[start_node], start_node))

    while queue:
        cur_distance, cur_node = heapq.heappop(queue)

        if cur_distance > distance[cur_node]:
            continue

        for nx_node, nx_distance in graph[cur_node]:
            gap_distance = cur_distance + nx_distance
            if gap_distance < distance[nx_node]:
                distance[nx_node] = gap_distance
                heapq.heappush(queue, (gap_distance, nx_node))
    return distance


N, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    node, node2, weight = map(int, sys.stdin.readline().split())
    graph[node].append([node2, weight])
    graph[node2].append([node, weight])

cross_node1, cross_node2 = map(int, sys.stdin.readline().split())

start_node = 1

# 경우 나누기
#시작-> 첫번째 거치는 노드 -> 두번째 거치는 노드 -> 마지막
#시작-> 두번째 거치는 노드 -> 첫번째 거치는 노드 -> 마지막
sample1 = dijkstra(start_node)[cross_node1] + dijkstra(cross_node1)[cross_node2] + dijkstra(cross_node2)[N]
sample2 = dijkstra(start_node)[cross_node2] + dijkstra(cross_node2)[cross_node1] + dijkstra(cross_node1)[N]

result = min(sample1, sample2)

if result >= INF:
    print(-1)
else:
    print(result)

