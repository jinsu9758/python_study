"""
[1] 입력이 떼어져서 온다

1  0 3 2  45
0 2 3 4 6


board = [list(map(int,input().split())) for _ in range(N)]


[2] 문자열로 와

RGBBB
GRBBB

board = [list(input()) for _ in range(N)]

-> 

board = [list(map(int, list(input()))) for _ in range(N)]

visit = [[0]* M for _ in range(N)]

visit = [[0]*M] * N #안 돼

[ [ 0,0,0,0,0]]
[ [0,0,0,1,0]]


for row in visit:
    print(row)
    
print(*visit, sep = "\n)


"""


#from collections import deque


N, M = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
#index 0 : 오, 1: 왼, 2 : 상, 3; 하

board = []

#queue = deque([[0, 0]])
queue = [[0, 0]]

visit = [[0] * M for _ in range(N)]

for i in range(N):
    num = list(map(int, input()))
    board.append(num)
    
#print(*board, sep = "\n")

board[0][0] = 1
visit[0][0] = 1

def bfs(board, queue):  #queue = [(0,0)]
    while queue:
        cur_x, cur_y = queue.pop(0)
        # visit_queue.append(q)
        for i in range(4):
            kx = cur_x + dx[i]
            ky = cur_y + dy[i]
            if kx >= 0 and kx < N and ky >=0 and ky < M:
                if board[kx][ky] == 1 and not visit[kx][ky]:
                    visit[kx][ky] = 1
                    board[kx][ky] = board[cur_x][cur_y] + 1
                    queue.append((kx,ky))

bfs(board, queue)
print(board[N-1][M-1])
