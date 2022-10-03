import sys

def up_num(num, length):
    num = str(num)
    for i in range(length-1):
        if num[i] > num[i+1]:
            return False
    return True

N = int(sys.stdin.readline())

dp = [[0]*10 for _ in range(81)]

ans = []

for _ in range(N):
    num = int(sys.stdin.readline())
    length = len(str(num))
    for i in range(81):
        for j in range(10):
            dp[i][j] = 0
    for i in range(1, 10):
        dp[0][i] = 1
        
    if up_num(num, length):
        for i in range(1, length):
            for j in range(1, 10):
                dp[i][j] = sum(dp[i-1]) - sum(dp[i-1][0:j])

        _sum = 0
        for i in range(length):
            _sum = _sum + sum(dp[i])
        for j in range(length):
            for k in range(num//10**(length-1-j)%10+1, 10):
                _sum -= dp[length-1-j][k]
        ans.append(_sum)
    else:
        ans.append(-1)

for a in ans:
    print(a)
        
