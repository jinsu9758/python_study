#메모리 초과
'''
N, r, c = map(int, input().split())

#print(N, r, c)

board = [[0 for _ in range(0, 2**N)] for _ in range(0, 2**N)]


num = (0, 0)
for i in range(0, 2**N):
    for j in range(0, 2**N):
        board[i][j] = (i, j)
        
#print(board)

cnt = 0
visit = []
def no_Find(x, y, N):
    global cnt
    #print(x, y, N)
    #print(board[x][y])
    if N != len(board):
        for i in range(x, x+N):
            for j in range(y, y+N):
                #cnt += 1
                #print(i, j)
                if (i, j) not in visit:
                    visit.append((i, j))
                if i==r and j==c:
                    return False
    return True
                
    


def Split(x, y, N):
    if N<1:
        return
    if no_Find(x, y, N):
        Split(x, y, N//2)
        Split(x, y+N//2, N//2)
        Split(x+N//2, y, N//2)
        Split(x+N//2, y+N//2, N//2)
        return
        
Split(0, 0, 2**N)

#print(visit)
for i in visit:
    cnt += 1
    #print(i)
    if i == (r, c):
        print(cnt-1)
        break
        
'''

N, r, c = map(int, input().split())

result = 0

def Split(x, y, n):
    global result
    if x == r and y == c:
        print(result)
        return

    if n == 1:
        result += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        result += n * n
        return
    Split(x, y, n//2)
    Split(x, y+n//2, n//2)
    Split(x+n//2, y, n//2)
    Split(x+n//2, y+n//2, n//2)
    
Split(0, 0, 2**N)















