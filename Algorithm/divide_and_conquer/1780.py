N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

def diff_box(x, y, N):
    tmp = board[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if tmp!=board[i][j]:
                return True
            else:
                tmp = board[i][j]
    return False


cnt = [0, 0, 0]
def Split(x, y, N):
    if N<1:
        return
    if diff_box(x, y, N):
        Split(x, y, N//3)
        Split(x+N//3, y, N//3)
        Split(x+2*(N//3), y, N//3)
        
        Split(x, y+N//3, N//3)
        Split(x+N//3, y+N//3, N//3)
        Split(x+2*(N//3), y+N//3, N//3)
        
        Split(x, y+2*(N//3), N//3)
        Split(x+N//3, y+2*(N//3), N//3)
        Split(x+2*(N//3), y+2*(N//3), N//3)
        return
    else:
        cnt[board[x][y]+1] += 1

Split(0, 0, N)
for i in cnt:
    print(i)
        
        
