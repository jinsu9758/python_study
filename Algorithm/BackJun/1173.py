N, m, M, T, R = map(int, input().split())

curr = m
cnt = 0
exer_cnt = 0
execute = 1
while True:
    if M - m < T:
        print(-1)
        execute = 0
        break
    else: # 실행가능
        cnt += 1
        if curr + T <= M:
            curr += T
            exer_cnt += 1
            #print(curr)
        elif curr + T > M:
            if curr - R <= m :
                curr = m
            else:
                curr -= R
            #print(curr)
        if exer_cnt == N:
            break
#print(cnt)

if execute:
    print(cnt)