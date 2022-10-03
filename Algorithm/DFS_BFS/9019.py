import sys
from collections import deque


# 입력
T = int(sys.stdin.readline())

cases = []
for _ in range(T):
    nums = list(map(int, sys.stdin.readline().split()))
    cases.append(nums)
#print(T, cases)

def make_D(node):
    node = node * 2
    if node > 9999:
        node = node % 10000
    return node

def make_S(node):
    if node == 0:
        node = 9999
    else:
        node = node - 1
    return node

# L, R  문자열로 처리하거나 deque의 rotate로 처리하면 시간초과 남.
def make_L(node):
    front = node // 1000
    end = node % 1000
    node = end*10+front
    return node


def make_R(node):
    end = node % 10
    front = node // 10
    node = end*1000+front
    return node



# 함수 생성
def bfs(case_list):
    start = case_list[0]
    target = case_list[1]
    queue = deque()
    visit = ['0' for _ in range(10000)]
    queue.append(start)
    visit[start] = ''
    
    while queue:
        node = queue.popleft()
        # D, S, L, R  다 적용해서 탐색
        node_D = make_D(node)
        node_S = make_S(node)
        node_L = make_L(node)
        node_R = make_R(node)


        if visit[node_D] == '0':
            visit[node_D] = visit[node] + 'D'
            queue.append(node_D)
            if node_D == target:
                return visit[target]
            
        if visit[node_S] == '0':
            visit[node_S] = visit[node] + 'S'
            queue.append(node_S)
            if node_S == target:
                return visit[target]
            
        if visit[node_L] == '0':
            visit[node_L] = visit[node] + 'L'
            queue.append(node_L)
            if node_L == target:
                return visit[target]
            
        if visit[node_R] == '0':
            visit[node_R] = visit[node] + 'R'
            queue.append(node_R)
            if node_R == target:
                return visit[target]
            
        
for t in range(T):
    print(bfs(cases[t]))