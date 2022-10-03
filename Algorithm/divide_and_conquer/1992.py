N = int(input())

board = [list(map(int, input())) for _ in range(N)]

#print(board)

def diff_box(x, y, N):
    tmp = board[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if tmp!=board[i][j]:
                return True
            else:
                tmp = board[i][j]
    return False


def Split(x, y, N):
    if N<1:
        return
    # 다른 숫자가 섞여있을 때
    if diff_box(x, y, N):
        print("(", end='')
        Split(x, y, N//2)
        Split(x, y+N//2, N//2)
        Split(x+N//2, y, N//2)
        Split(x+N//2, y+N//2, N//2)
        print(")", end='')
        return
    else: # 한 숫자로 일정할때
        print(board[x][y], end='')
#print(diff_box(0, 0, N))
Split(0, 0, N)