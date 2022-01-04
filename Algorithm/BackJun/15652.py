N, M = list(map(int, input().split()))

s = []

def dfs(start):
    if len(s) == M:
        #print(s)
        for l in range(M):
            if l == M-1:
                print(s[l])
                continue
            print(s[l], end=' ')
        return
    for i in range(start, N+1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)