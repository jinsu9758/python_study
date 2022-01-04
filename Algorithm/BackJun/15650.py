N, M = list(map(int, input().split()))

s = []

def back(start):
    if len(s) == M:
        for j in range(M):
            if j == M-1:
                print(s[j])
                continue
            print(s[j], end=' ')
        return
    for i in range(start, N+1):
        if i not in s:
            s.append(i)
            back(i+1)
            s.pop()
back(1)