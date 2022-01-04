M, N = map(int, input().split())

window_type = [0, 0, 0, 0, 0]

window_input = [input() for _ in range(5*M + 1)]

result = ""

result2 = []

for sero in range(0, 5*M+1):
    for garo in range(0, 5*N+1):
        if garo==0 or sero==0 or garo%5==0 or sero%5==0:
            pass
        else:
            result += window_input[sero][garo]

#print(result)
for i in range(0, len(result), 4):
    result2.append(result[i:i+4])

result3 = ['' for _ in range(N)]
for i in range(len(result2)):
    result3[i%N]+=result2[i]

#print(result3)

result4 = []
for i in result3:
    index = 0
    while index<16*M:
        result4.append(i[index:index+16])
        index+=16
#print(result4)
        

cnt_list = []
cnt = 0
for r in result4:
    index = 0
    while index<=12:
        if r[index:index+4] == "****":
            cnt += 1
        index += 4
    cnt_list.append(cnt)
    cnt=0

for j in cnt_list:
    if j==0:
        window_type[0] += 1
    elif j==1:
        window_type[1] += 1
    elif j==2:
        window_type[2] += 1
    elif j==3:
        window_type[3] += 1
    elif j==4:
        window_type[4] += 1
#print(window_type)

for i in window_type:
    print(i, end=' ')
