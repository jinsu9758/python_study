import sys
import math

#소수인지 아닌지 판별해주는 함수
def is_prime(x):
    if x==1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


T = int(sys.stdin.readline())

ans = []
for _ in range(T):
    n, k = map(int, sys.stdin.readline().split())
    prime = []
    dp = [[0]*(n+1) for _ in range(k+1)]
    
    # 소수 리스트 만들기
    for i in range(1, n+1):
        if is_prime(i):
            prime.append(i)

    dp[0][0] = 1

    #print(dp)

    for p in prime:
        for i in range(k, 0, -1):
            for j in range(n+1):
                if j-p < 0:
                    continue
                dp[i][j] += dp[i-1][j-p]
    #print(dp[k][n])
    ans.append(dp[k][n])

for a in ans:
    print(a)