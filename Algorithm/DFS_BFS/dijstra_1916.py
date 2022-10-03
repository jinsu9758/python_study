#다익스트라 예제문제 -2 < 백준 1916 >
import heapq
import sys

INF = sys.maxsize

def dijkstra(start_node):
    distance = [INF] * (N+1)
    queue = []
    distance[start_node] = 0
    heapq.heappush(queue, (distance[start_node], start_node))

    while queue:
        #print(queue)
        cur_distance, cur_node  = heapq.heappop(queue)

        if cur_distance > distance[cur_node]:
            continue

        for nx_node, nx_distance in graph[cur_node]:
            #print(nx_node, nx_distance)
            gap_distance = cur_distance + nx_distance
            if gap_distance < distance[nx_node]:
                distance[nx_node] = gap_distance
                heapq.heappush(queue, (gap_distance, nx_node))

    return distance


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    node, link_node, weight = map(int, sys.stdin.readline().split())
    graph[node].append([link_node, weight])
#print(graph)
start_node, end_node = map(int, sys.stdin.readline().split())

print(dijkstra(start_node)[end_node])
    
