import sys

N = int(sys.stdin.readline())

sum_point = [0 for _ in range(N+1)]
point = []
for _ in range(N):
    _case = int(sys.stdin.readline())
    point.append(_case)
if N==1:
    sum_point[1] = point[0]
elif N==2:
    sum_point[1] = point[0]
    sum_point[2] = point[0] + point[1]
elif N==3:
    sum_point[1] = point[0]
    sum_point[2] = point[0] + point[1]
    sum_point[3] = max(point[0]+point[2], point[1]+point[2])
else:
    sum_point[1] = point[0]
    sum_point[2] = point[0] + point[1]
    sum_point[3] = max(point[0]+point[2], point[1]+point[2])
    for i in range(4, N+1):
        sum_point[i] = max(sum_point[i-2]+point[i-1], sum_point[i-3]+point[i-2]+point[i-1])

print(sum_point[N])
