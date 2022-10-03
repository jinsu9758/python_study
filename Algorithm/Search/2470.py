# 35% INDEX ERROR
# 너무 끼워 맞춘 코드라서 반례가 상당히 많이 나올 수 있음. -> 다른 방법으로 구현
# 해야할 듯 싶음.
'''
import sys

N = int(sys.stdin.readline())
liq = list(map(int, sys.stdin.readline().split()))
liq.sort()

result, min = 0, 2000000000
result2 = [0, 0]

for l in liq:
    L = 0
    R = N
    while (L + 1 < R):
        M = (L + R)//2

        if liq[M] < -l:
            L = M
        else:
            R = M
    print(L, R)
    if L == N -1:
        R = L
        
    if liq[L] == l:
        if abs(liq[L-1] - l) <= abs(liq[R]-l):
            L = L - 1
        else:
            L = R
    if liq[R] == l:
        if abs(liq[L] - l) <= abs(liq[R+1]-l):
            R = L
        else:
            R = R+1

    if (liq[L] >= 0 and (-l) >= 0) or (liq[L] >= 0 and (-l) <= 0):
        res1 = abs(liq[L]-l)
    elif (liq[L] <= 0 and (-l)>=0) or (liq[L]<=0 and (-l) <= 0):
        res1 = abs(liq[L] + l)

    if (liq[R]>=0 and (-l)>=0) or (liq[R]>=0 and (-l) <= 0):
        res2 = abs(liq[R]-l)
    elif (liq[R]<=0 and (-l)>=0) or (liq[R]<=0 and (-l) <= 0):
          res2 = abs(liq[R]+l)

    if res1 <= res2:
        result = abs(liq[L] + l)
        if result <= min:
            min = result
            result2[0] = liq[L]
            result2[1] = l
    else:
        result = abs(liq[R] + l)
        if result <= min:
            min = result
            result2[0] = liq[R]
            result2[1] = l
result2.sort()
print(*result2)
'''          
    
# 맞았습니다. -> 일단은 최댓값 범위 신경써야함.
'''
중간값 + l 값 더해서 절댓값으로 작은거 값들 저장해주고, 0에 가깝게 L, R  옮겨줌.
여기서 중요한거는 liq[M], ㅣ이랑 같으면 안됨. 같으면 답이 이상하게 나옴.
해당 반례처리해주는거 중요함.
'''
import sys

N = int(sys.stdin.readline())
liq = list(map(int, sys.stdin.readline().split()))
liq.sort()

result, min = [0, 0], 2000000001

#print(N, liq)

for l in liq:
    L = 0
    R = N
    while L + 1 < R:
        M = (L + R) // 2
        #print(L, R, l)
        total = liq[M] + l
        #print(liq[M], l)
        if liq[M] != l:
            if abs(total) <= min:
                result[0] = liq[M]
                result[1] = l
                min = abs(total)
            if total < 0:
                L = M
            elif total > 0:
                R = M
            else:
                break
        else:
            if total < 0:
                L = M
            elif total > 0:
                R = M
            else:
                break
result.sort()
print(*result)