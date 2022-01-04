N, M, L = map(int, input().split())

N_dict = {}

N_dict[1] = 1
for i in range(2, N+1):
    N_dict[i] = 0

#print(N_dict) # {1: 1, 2: 0, 3: 0, 4: 0, 5: 0}
cnt = 0

i = 1
while True:
    if N_dict[i] == M:
        print(cnt)
        break
    if N_dict[i] % 2 == 1: # 홀수일 때
        if i + L > N:
            i = (i+L) % N
            N_dict[i] += 1
            cnt += 1
        else:
            i = i + L
            N_dict[i] += 1
            cnt += 1
    elif N_dict[i] % 2 == 0: #짝수일 때
        if i <= L: # 조건 조심!
            #print(i , N, L)
            i = i + N - L
            N_dict[i] += 1
            cnt += 1
        else:
            i = i - L
            N_dict[i] += 1
            cnt += 1
            
#print(N_dict)