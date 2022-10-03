import sys

n = int(sys.stdin.readline())

values = [0] * (n+1)


values[1] = 1

if n > 1:
    values[2] = 2

for i in range(3, n+1):
    values[i] = values[i-1] + values[i-2]

print(values[n]%10007)
