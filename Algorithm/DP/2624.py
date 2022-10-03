import sys

T = int(sys.stdin.readline())
k = int(sys.stdin.readline())

cnt = [[0]*(T+1) for _ in range(k)]
#print(cnt)

_input = []
for _ in range(k):
    p, n = map(int, sys.stdin.readline().split())
    _input.append([p, n])
    _input.sort()

#print(_input)

for i in range(1):
    coin, coin_cnt = _input[i][0], _input[i][1]
    for j in range(T+1):
        if j%coin==0 and j<=coin*coin_cnt:
            cnt[i][j] = 1
#print(cnt)

for i in range(1, k):
    coin, coin_cnt = _input[i][0], _input[i][1]
    cnt[i][0] = 1
    for j in range(1, T+1):
        cnt[i][j] = cnt[i-1][j]
        for c in range(1, coin_cnt+1):
            if j-coin*c >= 0:
                cnt[i][j] += cnt[i-1][j-coin*c]

print(cnt[k-1][T])
        
    

