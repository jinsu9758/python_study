# 반례
#https://www.acmicpc.net/board/view/24356

10 10 4
5 4
6 4
6 8
8 9
1 10
2 10
10 3
8 2
1 7
4 10

# 문자열로 넣으면 '5' > '10'임. 왜냐 앞자리만 비교해서 순서가 밀려남.
# 그래서 sort가 제대로 안됨.

import sys

N, M, V = map(int, sys.stdin.readline().split())

graph = {str(i):[] for i in range(1, N+1)}
graph2 = {str(i):[] for i in range(1, N+1)}

# 입력 받는 순서에 따라 답이 다르게 나옴.
nums_list = []
for _ in range(M):
    a,b = map(int,input().split())
    #print(str(a), b)
    graph[str(a)].append(b)
    graph[str(b)].append(a)
    graph2[str(a)].append(b)
    graph2[str(b)].append(a)

for i in range(1, N+1):
    graph[str(i)].sort(reverse=True)

for i in range(1, N+1):
    graph2[str(i)].sort()

#print(graph)
#print(graph2)

def dfs(graph, start_node):
    stack = []
    visit = []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        node = str(node)
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit

def bfs(graph, start_node):
    queue = []
    visit = []
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        node = str(node)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[str(node)])
    return visit

print(*dfs(graph, str(V)))
print(*bfs(graph2, str(V)))
