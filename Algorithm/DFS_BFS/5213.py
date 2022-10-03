import sys
from collections import deque

# 고려해야할꺼 좌우이동 / 위 아래 이동
def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    tile_num = tile[x][y][0]
    visit_cnt[tile_num] = 1
    while queue:
        #print(visit_node) #visit_node
        cur_x, cur_y = queue.popleft()
        #visit_node.append([cur_x, cur_y])
        if visit_node.get(tile[cur_x][cur_y][0]) == None:
            visit_node[tile[cur_x][cur_y][0]] = 1
        #print(visit_node)
        for i in range(2): # 좌우 탐색
            side_x = cur_x + dx[i]
            side_y = cur_y + dy[i]
            if (0<=side_x<=N-1 and 0<=side_y<=2*N-1):
                # 같은 타일에 위치할 때
                if tile[side_x][side_y][0] == tile[cur_x][cur_y][0] and visit_node.get(tile[side_x][side_y][0])==1:
                    queue.appendleft([side_x, side_y]) # 가중치가 없는 간선이라 무조건 먼저 넣어줘야함. (상-하는 먼저 넣어주면 순서가 꼬임. appendleft 무조건 써야함. 가중치 정렬 필수!!)
                    dir_node[side_x][side_y].append([cur_x, cur_y])
                    visit_node[tile[side_x][side_y][0]] = 2
                # 타일이 서로 다르고, 값은 같으며, 방문기록이 없는 경우!
                if tile[side_x][side_y][0] != tile[cur_x][cur_y][0] and tile[side_x][side_y][1] == tile[cur_x][cur_y][1] and visit_node.get(tile[side_x][side_y][0])==None:
                    queue.append([side_x, side_y])
                    visit_node[tile[side_x][side_y][0]] = 1 #
                    visit_cnt[tile[side_x][side_y][0]] = visit_cnt[tile[cur_x][cur_y][0]] + 1
                    dir_node[side_x][side_y].append([cur_x, cur_y])
        # 상하 탐색
        for j in range(2, 4):
            vert_x = cur_x + dx[j]
            vert_y = cur_y + dy[j]
            if (0<=vert_x<=N-1 and 0<=vert_y<=2*N-1):
                if tile[vert_x][vert_y][1] == tile[cur_x][cur_y][1] and visit_node.get(tile[vert_x][vert_y][0])==None:
                    #print(vert_x, vert_y)
                    queue.append([vert_x, vert_y])
                    visit_node[tile[vert_x][vert_y][0]] = 1 #
                    visit_cnt[tile[vert_x][vert_y][0]] = visit_cnt[tile[cur_x][cur_y][0]] + 1
                    dir_node[vert_x][vert_y].append([cur_x, cur_y])
       

N = int(sys.stdin.readline())

# 타일에 입력할꺼는  (타일의 번호, 타일의 숫자) 추가해주고있음.
tile = [[] for _ in range(N)]
cnt = 1
for i in range(N):
    #홀수번째 줄
    if (i+1)%2 == 1:
        for j in range(N):
            a, b = map(int, sys.stdin.readline().split())
            tile[i].append((cnt, a))
            tile[i].append((cnt, b))
            cnt += 1
    #짝수번째 줄 -> 빈 곳은 (-1, -1)로 채워줌
    elif (i+1)%2==0:
        tile[i].append((-1, -1))
        for j in range(N-1):
            a, b = map(int, sys.stdin.readline().split())
            tile[i].append((cnt, a))
            tile[i].append((cnt, b))
            cnt += 1
        tile[i].append((-1, -1))
        
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # 좌 우 상 하
visit_cnt = [0] * cnt # 타일 개수별로 visit_cnt 리스트 작성
visit_node = dict() # 방문한 노드
dir_node = [[[] for _ in range(2*N)] for _ in range(N)] # 노드 링크 리스트 (중요) -> 각 노드가 어디로 이동하는지 저장
route_node = []
bfs(0, 0)

#print(dir_node)

con = False
for i in range(N-1, -1, -1):
    for j in range(2*N-1, -1, -1):
        if dir_node[i][j]:
            x3 = i
            y3 = j
            x2 = i
            y2 = j
            while True:
                #print(x2, y2)
                if x2==0 and y2==0:
                    con = True
                    break
                tile_num = tile[x2][y2][0]
                #print(tile_num)
                if tile_num not in route_node:
                    route_node.append(tile_num)
                x2, y2 = dir_node[x2][y2][0]
        if con:
            break
    if con:
        break

#find_route(x2, y2)
route_node.reverse()
print(visit_cnt[tile[x3][y3][0]])
print(*route_node)


'''
[기존 코드의 문제점]
1. 시간 복잡도
- 재귀를 사용한거 (시간 복잡도 ㅈㄴ 늘어남)
- a in b_list 사용한거 -> 시간복잡도 N
ㄴ이라서 해당 코드 돌리게되면 O(N^2) 되버려서 당연히 시간 터짐

1번 해결법
결론 : 재귀함수 없애고, 딕셔너리를 사용하여 방문한 노드를 체크해주자!

2. queue.append 되는 순서
- 같은 타일에 위치하는 친구들 넣어주고
- 위아래 바뀌는 친구들 넣어주는 과정에서

* distance가 큰 노드들이 먼저 들어가는 경우가 일어날 수 있음.
따라서, 같은 타일에 위치하는 친구들은 distance가 똑같기 때문에 우선적으로 넣어주기 위해
appendleft()를 사용해주도록 하자....!

[불행중 다행인거]
-> 알고리즘 자체는 맞았다...!

'''