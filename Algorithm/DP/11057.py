import sys

N = int(sys.stdin.readline())

values = [[] for _ in range(N+1)]

values[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#print(values)

for n in range(2, N+1):
    values[n].append(sum(values[n-1]))
    for i in range(10):
        if i == 0:
            continue
        values[n].append(values[n][i-1]-values[n-1][i-1])

print(sum(values[N])%10007)


