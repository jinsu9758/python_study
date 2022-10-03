import sys

N = int(sys.stdin.readline())

k = int(sys.stdin.readline())

#print(N, k, PC_list)

graph = {str(i):[] for i in range(1, N+1)}
#print(graph)
for _ in range(k):
    a,b = map(int,input().split())
    graph[str(a)].append(str(b))
    graph[str(b)].append(str(a))
#print(graph)


def bfs(graph, start_node):
    queue = []
    visit = []
    queue.append(start_node)
    #visit.append(start_node)
    #print(queue)
    while queue:
        node = queue.pop(0)
        #print(node)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return len(visit)
        
        
print(bfs(graph, '1')-1)