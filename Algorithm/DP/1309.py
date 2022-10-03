import sys

N = int(sys.stdin.readline())

cage = [[] for _ in range(N+1)]

cage[1] = [1, 1, 1]

#print(cage)

for i in range(2, N+1):
    cage[i].append(sum(cage[i-1]))
    cage[i].append(cage[i-1][0] + cage[i-1][2])
    cage[i].append(cage[i-1][0] + cage[i-1][1])
    cage[i-2] = [] # 메모리 빼주기


print(sum(cage[N]) % 9901)    
