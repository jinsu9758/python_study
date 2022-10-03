import sys

T = int(sys.stdin.readline())
_case = []

for _ in range(T):
    E, W = map(int, sys.stdin.readline().split())
    _case.append([E, W])


for c in _case:
    e, w = c
    if e==1:
        print(w)
        continue
    
    dp = [[] for _ in range(w+1)]
    dp[1].append(1)
    
    for i in range(2, w+1):
        dp[i].append(i)
        dp[i].append(1)
    
    if w>=3:
        for i in range(3, w+1):
            for j in range(2, i):
                dp[i].insert(-1, dp[i-1][j-2] + dp[i-1][j-1])
    
    print(dp[w][e-1])