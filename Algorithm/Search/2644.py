# deque 사용하기
# https://dongdongfather.tistory.com/72



# 2644 촌수 계산  -> 이전에는  visit안에 node를 넣는 방법으로 식별했음.
# visit 리스트에 -> 숫자를 넣어줌으로써 구현할 것임.
# 일반 리스트에서 pop 형식으로 큐를 구현하면, 시간 복잡도가 N임.
# 이는 모든 원소들이 리스트에서 하나 빠져나가면 매꾸기 위해서 한칸씩 움직임.
# 이는 시간복잡도 O(N)임.
# deque를 사용하면, O(1)로 시간 복잡도를 줄일 수 있다! 그냥 앞에꺼 빼기만함.

import sys
from collections import deque

N = int(sys.stdin.readline())

start_node, dest_node = map(int, sys.stdin.readline().split())

M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)

visit = [0 for _ in range(N+1)]

def bfs(graph, start_node):
    queue = deque()
    queue.append(start_node)
    visit[start_node] += 1
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visit[i] == 0:
                visit[i] += visit[node] + 1 #첫번째 노드도 +1 됨. 나중에 1빼줘야함.
                queue.append(i)
    return visit

visit = bfs(graph, start_node)

if visit[dest_node] != 0:
    print(visit[dest_node]-1)
else:
    print(-1)

