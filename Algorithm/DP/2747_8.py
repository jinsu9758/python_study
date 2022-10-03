import sys
def fibo(N):
    if N==1 or N==2:
        return 1
    else:
        if fibo_value[N] != 0:
            return fibo_value[N]
        fibo_value[N] = fibo(N-1) + fibo(N-2)
        return fibo_value[N]

N = int(sys.stdin.readline())
fibo_value = [0] * (N+1)
print(fibo(N))