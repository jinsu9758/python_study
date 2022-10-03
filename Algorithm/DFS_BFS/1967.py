import sys
from collections import deque

def dfs(start_node):
    stack = deque()
    visit_node = dict()
    visit_cnt = [0 for _ in range(N+1)]
    stack.append(start_node)
    visit_cnt[start_node] = 0
    visit_node[start_node] = 1
    while stack:
        node = stack.pop()
        for nx_node, nx_weight in graph[node]:
            if visit_node.get(nx_node) == None:
                stack.append(nx_node)
                visit_cnt[nx_node] = visit_cnt[node] + nx_weight
                visit_node[nx_node] = 1
    return visit_cnt
    

def find_far_node(far_node):
    _max = -1
    max_index = -1
    result = []
    for f in range(1, len(far_node)):
        if _max <= far_node[f]:
            _max = far_node[f]
            max_index = f
    result.append(_max)
    result.append(max_index)
    return result
        


N = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    node, link_node, weight = map(int, sys.stdin.readline().split())
    graph[node].append([link_node, weight])
    graph[link_node].append([node, weight])

#print(graph)

far_node = dfs(1)
far_node2 = find_far_node(far_node)
far_node = dfs(far_node2[1])
result = find_far_node(far_node)
print(result[0])
