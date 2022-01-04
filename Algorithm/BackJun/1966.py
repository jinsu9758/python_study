import copy

case = int(input())

queue = []

num_list = []

M_list = []
for i in range(case):
    N, M = map(int, input().split()) #N은 문서의 개수, M은 몇번째에 있는
    M_list.append(M)
    num = list(map(int, input().split()))
    num_list.append(num)
#print(num_list)

queue = copy.deepcopy(num_list)

#print(queue)
#print(M_list)
#print(num_list[0][M_list[0]])
cnt_list = []
for i, que in enumerate(queue):
    #print(i, que)
    index = [0 for _ in range(len(que))]
    index[M_list[i]] = 1  # 같은경우일때 구분을 위해 인덱스도 고려해야함.
    cnt = 0
    while True:
        if que[0] == max(que):
            answer = que.pop(0)
            #print(num_list)
            answer2 = index.pop(0)
            cnt += 1
            if answer == num_list[i][M_list[i]] and answer2 == 1:
                break
        elif que[0] < max(que):
            behind = que.pop(0)
            que.append(behind)
            behind2 = index.pop(0)
            index.append(behind2)
    cnt_list.append(cnt)
    
for l in cnt_list:
    print(l)