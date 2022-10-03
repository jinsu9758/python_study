import sys

n, k = map(int, sys.stdin.readline().split())

dp = [0]*(k+1)

a = int(sys.stdin.readline())

for i in range(0, k+1):
    if i%a == 0:
        dp[i] = 1
#print(dp)

for _ in range(1, n):
    a = int(sys.stdin.readline())
    for j in range(a, k+1):
        dp[j] += dp[j-a]
print(dp[k])
    

# 메모리 초과
'''
a = int(sys.stdin.readline())
for i in range(0, k+1):
    if i%a == 0:
        dp[0][i] = 1
    

for i in range(1, n):
    a = int(sys.stdin.readline())
    
    for j in range(0, a):
        dp[i][j] = dp[i-1][j]
    for z in range(a, k+1):
        dp[i][z] = dp[i-1][z] + dp[i][z-a]
    dp[i-1] = []

print(dp[n-1][k])
'''
