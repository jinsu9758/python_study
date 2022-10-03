import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N+1)]

dp[0] = 1
for i in range(2, N+1, 2):
	dp[i] = 3*dp[i-2]
	for j in range(0, i-3, 2):
		dp[i] += dp[j]*2
print(dp[N])