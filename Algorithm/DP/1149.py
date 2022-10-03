import sys

N = int(sys.stdin.readline())

dp = [[0, 0, 0] for _ in range(N)]

for i in range(N):
    colors = list(map(int, sys.stdin.readline().split()))

    if i == 0:
        dp[i][0] = colors[0]
        dp[i][1] = colors[1]
        dp[i][2] = colors[2]
    else:
        for j in range(3):
            _min = 987654321
            for k in range(3):
                if j == k:
                    continue
                if _min >= dp[i-1][k]:
                    _min = dp[i-1][k]
            dp[i][j] = _min + colors[j]
            
                
        
print(min(dp[N-1]))