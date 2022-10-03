import sys

def dp(n):
    for i in range(3, n+1):
        values.append(values[i-3] + values[i-2] + values[i-1])
    return values[n]



T = int(sys.stdin.readline())

_case = []
for _ in range(T):
    n = int(sys.stdin.readline())
    _case.append(n)

for c in _case:
    values = [1, 1, 2]
    print(dp(c))
