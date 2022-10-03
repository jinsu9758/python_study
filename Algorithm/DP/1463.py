import sys

values = [0, 0]

N = int(sys.stdin.readline())

for i in range(2, N+1):
    result = []
    if i%2==0:
        result.append(values[i//2] + 1)
    if i%3==0:
        result.append(values[i//3] + 1)
    result.append(values[i-1] + 1)
    _min = min(result)
    values.append(_min)

print(values[N])


