def equal_color(board):
    #print(board)
    tmp = board[0][0]
    for index1 in range(len(board)):
        for index2 in range(len(board[index1])):
            if tmp != board[index1][index2]:
                return True
            else:
                tmp = board[index1][index2]
    return False


cnt = [0, 0]
def Split(board, N):
    board1, board2, board3, board4 = [], [], [], []

    if N < 1:
        return
    
    if equal_color(board):
        #index1 = len(board)//2
        N = N//2
        #print("색깔 다른거 존재")
        # 나눠야 됨. -> 사분면 별로 나눠야 할 듯?
        #1 사분면
        for i in range(0, N):
            str = []
            for j in range(0, N):
                str.append(board[i][j])
            board1.append(str)
        Split(board1, N)

        #2사분면
        for i in range(N, 2*N):
            str = []
            for j in range(0, N):
                str.append(board[i][j])
            board2.append(str)
        Split(board2, N)

        #3사분면
        for i in range(0, N):
            str = []
            for j in range(N, 2*N):
                str.append(board[i][j])
            board3.append(str)
        Split(board3, N)

        #4사분면
        for i in range(N, 2*N):
            str = []
            for j in range(N, 2*N):
                str.append(board[i][j])
            board4.append(str)
        Split(board4, N)
    else:
        #print("색깔 동일")
        cnt[board[0][0]] += 1
        return


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
Split(board, N)     
#print(cnt)

for c in cnt:
    print(c)




'''
import sys

N = int(sys.stdin.readline())
P = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []

def solution(x, y, N):
    color = P[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != P[i][j]:
                solution(x,y,N//2)
                solution(x,y+N//2,N//2)
                solution(x+N//2,y,N//2)
                solution(x+N//2,y+N//2,N//2)
                return
    if color == 0:
        result.append(0)
    elif color == 1:
        result.append(1)

if '__main__' == __name__:
    solution(0,0,N)
    print(result.count(0))
    print(result.count(1))
'''
