#문제 잘못읽음. 도로는 방향이 없고, 웜홀은 방향이 있음.
#+ 입력값을 잘못 입력함.
import sys

INF = sys.maxsize


def bellmanford(start_node):
    distance = [INF] * N
    distance[start_node - 1] = 0
    minus_cycle = False
    
    for _ in range(N-1):
        for node in graph:
            s, e, t = node
            if distance[e-1] > distance[s-1] + t:
                distance[e-1] = distance[s-1] + t
    for node in graph:
        s, e, t = node
        if distance[e-1] > distance[s-1] + t:
            minus_cycle = True
            return minus_cycle    
    return minus_cycle



TC = int(sys.stdin.readline())

for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    graph =[]
    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        graph.append([S, E, T])
        graph.append([E, S, T])
    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        graph.append([S, E, -1*T])


    key = bellmanford(1)

    if key:
        print("YES")
    else:
        print("NO")
