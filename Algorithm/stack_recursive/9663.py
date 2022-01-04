#퀸을 놓아도 되는지 탐색을 해주는 함수
def avail(x):
    for i in range(x):
        if board[x]==board[i] or abs(board[x]-board[i]) == abs(x-i):
            return False
    return True
    
    
cnt = 0
def dfs(x): #x : 몇번째 줄의 board를 보고 있는지
    global cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):
        #print(i)
        board[x] = i
        if avail(x):
            dfs(x+1)

N = int(input())
board = [0 for _ in range(N)]
dfs(0)
print(cnt)
    
    
'''
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[int(input())])
'''
