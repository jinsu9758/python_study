import sys

INF = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    city1, city2, pay = map(int, sys.stdin.readline().split())
    graph[city1].append([city2, pay])

#print(graph)

floyd = [[INF]*n for _ in range(n)]


# 1. 같은 도시로 가는 경우는 0으로 초기화 하기.
for i in range(n):
    for j in range(n):
        if i==j:
            floyd[i][j] = 0

#print(floyd)

'''
print(graph)
[[], [[2, 2], [3, 3].......]]
'''

'''
for f in floyd:
    print(f)
[0, 'INF', 'INF', 'INF', 'INF']
['INF', 0, 'INF', 'INF', 'INF']
['INF', 'INF', 0, 'INF', 'INF']
['INF', 'INF', 'INF', 0, 'INF']
['INF', 'INF', 'INF', 'INF', 0]
'''

# 2. 직진 경로 업데이트 해주기

for i in range(1, n+1):
    for g in graph[i]:
        floyd[i-1][g[0]-1] = min(floyd[i-1][g[0]-1], g[1])

# 3. 각 노드 한번씩 거쳐서 최솟값 구하기
for k in range(1, n+1): #1~n까지 노드 중 거치는 노드
    for i in range(1, n+1):
        for j in range(1, n+1):
            floyd[i-1][j-1] = min(floyd[i-1][j-1], floyd[i-1][k-1] + floyd[k-1][j-1])

for f in range(len(floyd)):
    for f2 in range(n):
        if floyd[f][f2] >= INF:
            floyd[f][f2] = 0

for f in floyd:
    print(*f)