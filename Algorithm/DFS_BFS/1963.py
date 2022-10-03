import sys
from collections import deque
import math

#입력
T = int(sys.stdin.readline())

cases = []
for _ in range(T):
    nums = list(map(int, sys.stdin.readline().split()))
    cases.append(nums)

#print(T, cases)

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False # 소수가 아님
    return True


def cnt_alp(i, node):
    cnt = 0
    i = str(i)
    node = str(node)
    if i[0] == node[0]:
        cnt += 1
    if i[1] == node[1]:
        cnt += 1
    if i[2] == node[2]:
        cnt += 1
    if i[3] == node[3]:
        cnt += 1
    return cnt



def bfs(case1):
    start = case1[0]
    target = case1[1]
    #print(start, target)
    queue = deque()
    visit = [0 for _ in range(1000, 10000)]
    queue.append(start)
    visit[start-1000] = 1
    #print(visit)
    while queue:
        node = queue.popleft()
        for i in range(4): #자리수
            if i == 0: # 천의 자리 수 변경
                for j in range(1, 10):
                    new_node = str(j)+str(node)[1:4]
                    new_node = int(new_node)
                    if is_prime_number(new_node) and cnt_alp(node, new_node)==3 and visit[new_node-1000]==0:
                        #print(node, new_node)
                        visit[new_node-1000] = visit[node-1000] + 1
                        queue.append(new_node)
            elif i==1:
                for j in range(0, 10):
                    new_node = str(node)[0]+str(j)+str(node)[2:4]
                    new_node = int(new_node)
                    if is_prime_number(new_node) and cnt_alp(node, new_node)==3 and visit[new_node-1000]==0:
                        #print(node, new_node)
                        visit[new_node-1000] = visit[node-1000] + 1
                        queue.append(new_node)
            elif i==2:
                for j in range(0, 10):
                    new_node = str(node)[0:2]+str(j)+str(node)[3]
                    new_node = int(new_node)
                    if is_prime_number(new_node) and cnt_alp(node, new_node)==3 and visit[new_node-1000]==0:
                        #print(node, new_node)
                        visit[new_node-1000] = visit[node-1000] + 1
                        queue.append(new_node)
            elif i==3:
                for j in range(0, 10):
                    new_node = str(node)[0:3]+str(j)
                    new_node = int(new_node)
                    if is_prime_number(new_node) and cnt_alp(node, new_node)==3 and visit[new_node-1000]==0:
                        #print(node, new_node)
                        visit[new_node-1000] = visit[node-1000] + 1
                        queue.append(new_node)
    return visit[target-1000] - 1

for i in range(T):
    print(bfs(cases[i]))
