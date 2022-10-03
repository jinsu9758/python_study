import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())


L = 1
R = N**2

while L<=R:
    M = (L + R)//2
    result2 = 0
    for i in range(1, N+1):
        result1 = M // i
        if result1 >= N:
            result2 += N
        elif result1 < N:
            result2 += result1

    if k <= result2 :
        R = M - 1
    elif k > result2:
        L = M + 1
print(L)