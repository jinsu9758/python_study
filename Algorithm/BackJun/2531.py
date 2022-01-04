'''
#시간초과? # 투 포인트
import sys
N, d, k, c = map(int, sys.stdin.readline().rsplit())

susies = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
#print(susies)


ano_susi = []
for index in range(N):
    left = 0
    right = 1
    choice_susi = []
    if index+k <= N:
        choice_susi = susies[index:index+k]
    elif index+k > N:
        choice_susi += susies[index:index+(k-(index+k-N))]
        choice_susi+= susies[(index+(k-(index+k-N)))%8:(index+k)%N]

    #print(choice_susi)
    cnt = 0
    for i in range(len(choice_susi)):
        for j in range(i+1, len(choice_susi)):
            #print(choice_susi[i], choice_susi[j])
            if choice_susi[i] == choice_susi[j]:
                cnt+=1
    while right<=3:
        if right == 3:
            left+=1
        if choice_susi[left] == choice_susi[right] and right-left<=3:
            cnt+=1
            break
        elif choice_susi[left] != choice_susi[right] and right-left<=3:
            right+=1
    if cnt == 0:
        ano_susi.append(choice_susi)

max_len = 0
for ano in ano_susi:
    ano += [c]
    ano = list(set(ano))
    #print(ano)
    if max_len < len(ano):
        max_len = len(ano)
print(max_len)

'''
#시간초과
'''
import sys

#입력 받기
N, d, k, c = map(int, sys.stdin.readline().rsplit())
susies = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

#투 포인터 사용사기
lp = 0
rp = 0

while lp!=N:
    rp = lp + k
    susi= []
    add = True
    for i in range(lp, rp):
        i%=N
        susi.append(susies[i])
        if susies[i] == c:
            add = False
    cnt = len(susi)
    if add:
        cnt += 1
    result = max(0, cnt)
    lp+=1
print(result)        



'''
'''
from collections import defaultdict
N, d, k, c = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

canEat = defaultdict(int)
cnt = 1
for i in range(k):
    if canEat[arr[i]]==0:
        cnt+=1
    canEat[arr[i]] += 1
answer = cnt

for left in range(N):
    right = (left+k)%N
    canEat[arr[left]] -= 1
    if canEat[arr[left]] == 0:
        cnt -= 1
    if canEat[arr[right]] == 0:
        cnt += 1
    canEat[arr[right]] += 1
    answer = max(answer, cnt)
print(answer)
'''



import sys

#입력 받기
N, d, k, c = map(int, sys.stdin.readline().rsplit())
susies = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

#투 포인터 사용사기
lp = 0
rp = 0
result = 0
while lp!=N:
    rp = lp + k
    susi= set() #중복 제거
    add = True
    for i in range(lp, rp):
        i%=N
        susi.add(susies[i])
        if susies[i] == c:
            add = False
    cnt = len(susi)
    if add:
        cnt += 1
    result = max(result, cnt)
    lp+=1
print(result)



