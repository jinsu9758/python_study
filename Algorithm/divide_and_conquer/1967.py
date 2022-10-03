n = int(input())
graph = {i:[] for i in range(n+1)}


for i in range(n-1):
    node, sub_node, depth = map(int, input().split())
    graph[node].append((sub_node, depth))

print(graph)
