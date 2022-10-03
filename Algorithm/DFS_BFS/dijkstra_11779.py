import heapq
import sys

INF = sys.maxsize

def dijkstra(start_node):
    distance = [INF] * (n+1)
    queue = []
    distance[start_node] = 0
    heapq.heappush(queue, (distance[start_node], start_node))

    while queue:
        cur_distance, cur_node = heapq.heappop(queue)
        
        if cur_distance > distance[cur_node]:
            continue

        for nx_node, nx_distance in graph[cur_node]:
            gap_distance = cur_distance + nx_distance
            if distance[nx_node] > gap_distance:
                distance[nx_node] = gap_distance
                heapq.heappush(queue, (gap_distance, nx_node))
                visit_node[nx_node] = []
                visit_node[nx_node].append(cur_node)
    return distance


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visit_node = [[] for _ in range(n+1)]
route = []
for _ in range(m):
    city1, city2, pay = map(int, sys.stdin.readline().split())
    graph[city1].append([city2, pay]) # 단방향임.
    #graph[city2].append([city1, pay])
    
a, b = map(int, sys.stdin.readline().split())

#print(graph)

print(dijkstra(a)[b])
#print(visit_node)

end = b
while True:
    pre_node = visit_node[end]
    #print(pre_node)
    if pre_node == []:
        break
    else:
        route.append(pre_node[0])
        end = pre_node[0]
route.reverse()
route.append(b)
print(len(route))
print(*route)
        

