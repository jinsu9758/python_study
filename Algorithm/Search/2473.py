import sys

N = int(sys.stdin.readline())

liq = list(map(int, sys.stdin.readline().split()))

liq.sort()
#print(N, liq)
result, min = [0, 0, 0], 4000000001

for i in range(0, len(liq)-1):
    for j in range(i+1, len(liq)):
        #print(i, j) #2개 뽑기
        target = liq[i] + liq[j]
        L = 0
        R = N - 1
        while L <= R:
            M = (L+R)//2
            total = liq[M] + target
            if liq[M] != liq[i] and liq[M]!=liq[j]:
                if abs(total) <= min:
                    result[0] = liq[i]
                    result[1] = liq[j]
                    result[2] = liq[M]
                    min = abs(total)
                if total > 0 :
                    R = M - 1
                elif total < 0:
                    L = M + 1
                else:
                    break
            else:
                if total > 0 :
                    R = M - 1
                elif total < 0:
                    L = M + 1
                else:
                    break
result.sort()
print(*result)
                
            
            
        
        
