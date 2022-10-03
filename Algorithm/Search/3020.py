#첫번째 풀이
import sys

N, H = map(int, sys.stdin.readline().split())
length_list = [int(sys.stdin.readline()) for _ in range(N)]

#print(N, H, length_list)
down_to_up = []
up_to_down = []

for l in range(len(length_list)):
    if l%2 == 0:
        down_to_up.append(length_list[l])
    else:
        up_to_down.append(length_list[l])

#print(down_to_up, up_to_down)
        
# 구간의 차이를 계산하기 위해서 가상의 값을 집어넣어주기.
# 석순 넣어줬으니까 종유석 집어넣어줘야함.

down_to_up.append(0)
down_to_up.append(H)
up_to_down.append(0)
up_to_down.append(H)



down_to_up.sort()
up_to_down.sort()

#print(down_to_up, up_to_down) #0 1 3 5 7

dtu_len = len(down_to_up) #5
utd_len = len(up_to_down) #5
#print(dtu_len, utd_len)

min = 10000000
cnt = 0 # 최소 파괴를 갖는 라인별 횟수
for i in range(dtu_len-1, 0, -1):
    destroy_cnt = dtu_len - i - 1 # 석순의 파괴 개수
    #print(destroy_cnt)  #가상의 값을 집어넣어줌으로써, 파괴 횟수도 잘 나옴. 0 1 2 3

    #석순의 파괴 개수에 따른 종유석 최솟값 구하기.
    target = H - down_to_up[i-1] #무조건 최소는 구간별 첫번째 줄임.
    L = 0
    R = utd_len - 1 #
    while L<=R:
        M = (L + R)//2
        if target <= up_to_down[M]:
            R = M - 1
        elif up_to_down[M] < target:
            L = M + 1
    #print(L)
    #print(utd_len-L) # destroy_cnt에 따른 구간별 최소 종류석의 개수
    utd_cnt = utd_len-L-1 # 가상으로 집어 넣어준거 1개 빼주기
    #print(utd_cnt)
    if destroy_cnt + utd_cnt < min:
        min = destroy_cnt + utd_cnt
        cnt = H - up_to_down[L-1] - down_to_up[i-1] # 구간의 차이 -> 최소값의 개수
    elif destroy_cnt + utd_cnt == min:
        cnt += H - up_to_down[L-1] - down_to_up[i-1]
print(min, cnt)

#두번째 풀이
'''
import sys

N, H = map(int, sys.stdin.readline().split())
length = [int(sys.stdin.readline()) for _ in range(N)]

#print(N, H, length)

down_to_up = []
up_to_down = []

for l in range(len(length)):
    if l%2 == 0:
        down_to_up.append(length[l])
    else:
        up_to_down.append(length[l])

#print(down_to_up, up_to_down)

down_to_up.sort()
up_to_down.sort()

min = 1000000
cnt = 0
for height in range(1, H+1):
    #석순 개수 세기
    L = 0
    R = N//2 - 1
    dtu_cnt = 0
    while L<=R:
        M = (L + R)//2
        if height <= down_to_up[M]:
            R = M - 1
        elif down_to_up[M] < height:
            L = M + 1
    if L >= N//2:
        dtu_cnt += 0
    else:
        dtu_cnt += N//2 - L
    #print(dtu_cnt)

    #종유석 개수 세기
    L = 0
    R = N//2 - 1
    utd_cnt = 0
    height = H-height+1
    #print(height)
    while L<=R:
        M = (L + R)//2
        if height <= up_to_down[M]:
            R = M - 1
        elif up_to_down[M] < height:
            L = M + 1
    #print(L)
    
    if L >= N//2:
        utd_cnt += 0
    else:
        utd_cnt += N//2 - L
    #print(utd_cnt)

    if dtu_cnt + utd_cnt < min:
        min = dtu_cnt + utd_cnt
        cnt = 1
    elif dtu_cnt + utd_cnt == min:
        cnt += 1
print(min, cnt)
'''