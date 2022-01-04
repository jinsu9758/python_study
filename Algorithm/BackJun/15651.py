# 중복 순열

N, M = list(map(int, input().split()))

s = []

def dfs():
    if len(s) == M:
        #print(s)
        for m in range(M):
            if m == M-1:
                print(s[m])
                continue
            print(s[m], end=' ')
        return
    for i in range(1, N+1):
        s.append(i)
        dfs()
        s.pop()

dfs()