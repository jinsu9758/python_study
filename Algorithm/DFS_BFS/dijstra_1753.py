#다익스트라 예제문제 -1 < 백준 1753 >

import heapq
import sys

INF = sys.maxsize



def dijkstra(start_node):
    distance = [INF] * (V+1)
    queue = []
    distance[start_node] = 0
    heapq.heappush(queue, (distance[start_node], start_node))

    while queue:
        cur_distance, cur_node = heapq.heappop(queue)

        if cur_distance > distance[cur_node]:
            continue

        for next_node, next_distance in graph[cur_node]:
            #print(next_node, next_distance)
            gap_distance = cur_distance + next_distance
            if gap_distance < distance[next_node]:
                distance[next_node] = gap_distance
                heapq.heappush(queue, (gap_distance, next_node))
    return distance
    

V, E = map(int, sys.stdin.readline().split())
start_node = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    node, link_node, weight = map(int, sys.stdin.readline().split())
    graph[node].append([link_node, weight])


#print(dijkstra(start_node))
for i in dijkstra(start_node)[1:V+1]:
    if i == INF:
        print('INF')
    else:
        print(i)
