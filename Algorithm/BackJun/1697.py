from collections import deque

N, K = map(int, input().split())
Max = 100001
cnt = [0] * Max

def bfs(n):
    deque_list = deque()
    deque_list.append(n)
    while deque_list:
        visit_node = deque_list.popleft()
        if visit_node == K:
            print(cnt[K])
            return
        for nx in (visit_node-1, visit_node+1, 2*visit_node):
            if 0<= nx < Max and not cnt[nx]: #조건 이렇게 안써주면 런타임 에러남....
                cnt[nx] = cnt[visit_node] + 1
                deque_list.append(nx)
            

bfs(N)     