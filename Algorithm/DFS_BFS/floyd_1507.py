import sys

N = int(sys.stdin.readline())


# 입력 값으로 이미 최소 값들은 구해진 상태임.
# 우리가 구해야하는것은 도로개수가 최소가 될때의 합
dist = []
for _ in range(N):
    _input = list(map(int, sys.stdin.readline().split()))
    dist.append(_input)


# 도로의 개수 최소로 어떻게 만들 것인가?
# 기본 아이디어
'''
k : 지나가는 도시
i : 출발 도시
j : 도착 도시

i->j의 시간 == i->k->j 이면, i->j로 가는 길은 필요가 없음.
ㄴ(모든 노드가 다 지날 수 있어야하며, 최소가 되어야함.)

i->j시간 > i->k->j시간이면, 노드이동간의 최소 시간이 아니므로, 애초에 입력값이
잘못되었다고 할 수 있음.
'''
unused = []

avail = True
for k in range(N):
    for i in range(N):
        for j in range(N):
            if k==i or i==j or k==j:
                continue
            elif dist[i][j] == dist[i][k] + dist[k][j]:
                unused.append([i, j])
            elif dist[i][j] > dist[i][k] + dist[k][j]:
                avail = False

if avail:
    ans = 0
    for i in range(N):
        for j in range(N):
            if [i, j] in unused:
                continue
            else:
                ans += dist[i][j]
    print(ans//2)
else:
    print(-1)
                

