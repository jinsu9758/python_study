
M = int(input())

change = [list(map(int, input().split())) for _ in range(M)]

#print(change)

ball = 1 # 공이 있는 위치

cup = [1, 2, 3]
#print()
for ch in change:
    x, y = ch
    #print(x, y)
    X = cup.index(x)
    Y = cup.index(y)
    cup[X], cup[Y] = cup[Y], cup[X]

print(cup[ball-1])
             
