def hanoi(N, start, dest, pre):
    if N == 1:
        print(start, dest)
        return
    hanoi(N-1, start, pre, dest)
    print(start, dest)
    hanoi(N-1, pre, dest, start)


n = int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)
