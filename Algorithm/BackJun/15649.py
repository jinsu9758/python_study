
N, M = list(map(int, input().split()))

s = [0 for i in range(M)]

def dfs(k):
    if k == M:
        for j in range(M):
            if j == M-1:
                print(s[j])
                continue
            print(s[j], end=" ")
        return
    for i in range(1, N+1):
        if i not in s:
            s[k] = i
            dfs(k+1)
            s.append(0)
            s.pop(k+1)

dfs(0)


#itertools를 이용하여 구해보기
# import itertools

# N, M = map(int, input().split())

# number = []

# for i in range(1, N+1):
#     number.append(i)

# c = itertools.permutations(number, M)

# #print(list(c))

# for i in list(c):
#     i = str(i)
#     print(i.replace('(', '').replace(')', '').replace(',', ''))
    