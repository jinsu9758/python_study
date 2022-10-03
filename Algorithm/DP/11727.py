import sys

n = int(sys.stdin.readline())

values = [0] * (n+1)


values[1] = 1

if n > 1:
    values[2] = 3

for i in range(3, n+1):
    values[i] = values[i-2]*2 + values[i-1]

print(values[n]%10007)
