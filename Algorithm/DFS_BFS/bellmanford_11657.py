import sys

INF = sys.maxsize

N, M = map(int, sys.stdin.readline().split())

graph = []
distance = [INF] * N

#입력 받기
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append([a, b, c])


#사이클 돌기
def bellman(start_node):
    # 시작노드 -> 시작노드 : 0
    distance[start_node-1] = 0
    # V-1만큼 먼저 돌기
    for _ in range(N-1):
        for node in graph:
            s, e, d = node
            #무조건 1부터 시작해야하니까 첫 시작이 무한인 경우 막아줌 -> 어차피 다음 사이클때 계산됨.
            if distance[s-1]!=INF and distance[e-1] > distance[s-1] + d:
                distance[e-1] = distance[s-1] + d
                
    # 음의 사이클인지 확인하기
    for node in graph:
        s, e, d = node
        if distance[s-1]!=INF and distance[e-1] > distance[s-1] + d:
            return -1

    for d in range(len(distance)):
        if distance[d] == INF:
            distance[d] = -1
    #print(distance)
    return 1
        
if bellman(1) == -1:
    print(-1)
else:
    for d in distance[1:]:
        print(d)
    
    
