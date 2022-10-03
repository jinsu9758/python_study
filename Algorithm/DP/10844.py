import sys

N = int(sys.stdin.readline())

values = [[] for _ in range(N+1)]

values[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

for n in range(2, N+1):
    for i in range(0, 10):
        values[n].append(values[n-1][i-1] + values[n-1][i+1])
    values[n].append(0)

print(sum(values[N])%1000000000)
