# 입력
R, S = map(int, input().split())

Bench = [list(input().split()) for _ in range(R)]

handsk = [[0 for _ in range(S)] for _ in range(R)]

Bench2 = []
for i in range(len(Bench)):
    Bench2.append([x for x in str(Bench[i])[2:2+S]])


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, -0, 1, -1, 1, -1, 0, 1]

for index1 in range(R):
    for index2 in range(S):
        if Bench2[index1][index2] == "o":
            for i in range(8):
                if 0<=index1+dx[i]<=R-1 and 0<=index2+dy[i]<=S-1:
                    if Bench2[index1+dx[i]][index2+dy[i]] == "o":
                        pass
                    else:
                        handsk[index1+dx[i]][index2+dy[i]] += 1

#print(handsk)   
pos_num = 0
for hand in handsk:
    for h in hand:
        if pos_num < h:
            pos_num = h

#print(pos_num)
pos_index = []

for i in range(R):
    for j in range(S):
        if handsk[i][j] == pos_num:
            pos_index.append([i, j])

#print(pos_index)            
# 악수 횟수 구하기
max_cnt = []
for pos in pos_index:
    x,y = pos
    Bench2[x][y]="o"
    #print(Bench2)
    cnt = 0
    for I in range(R):
        for J in range(S):
            if Bench2[I][J] == "o":
                #print(I, J)
                for m in range(8):
                    if 0<=I+dx[m]<=R-1 and 0<=J+dy[m]<=S-1 and Bench2[I+dx[m]][J+dy[m]]=="o":
                        #print(I+dx[m], J+dy[m])
                        cnt+=1
    max_cnt.append(cnt)
    Bench2[x][y]="."

print(max(max_cnt)//2)
