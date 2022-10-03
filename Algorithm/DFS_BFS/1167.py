import sys
from collections import deque

def dfs(start_node):
    stack = deque()
    visit_node = dict()
    visit_distance = [0] * (N+1)
    visit_node[start_node] = 1
    stack.append(start_node)
    visit_distance[start_node] = 0
    while stack:
        node = stack.pop()
        for g in graph[node]:
            nx_node , nx_distance = g
            if visit_node.get(nx_node) == None:
                stack.append(nx_node)
                visit_distance[nx_node] = visit_distance[node] + nx_distance
                visit_node[nx_node] = 1
    return visit_distance
            

def find_max_node(distance):
    result = []
    _max = -1
    _max_index = -1
    for r in range(1, len(distance)):
        if _max <= distance[r]:
            _max = distance[r]
            _max_index = r
    result.append(_max)
    result.append(_max_index)
    return result


N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    node_info = list(map(int, sys.stdin.readline().split()))
    list_len = len(node_info)
    for j in range(1, list_len-2, 2):
        graph[node_info[0]].append(node_info[j:j+2])
        
#print(graph)
dir_node = [[] for _ in range(N)]
result_visit = dfs(1)
r = find_max_node(result_visit)
#print(r)
result = dfs(r[1])
result = find_max_node(result)
print(result[0])

    
