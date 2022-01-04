A, B = input().split()

A_list = ['' for _ in range(len(B))]
B_list = list(B)

A_lists = []

for a in range(len(A)):
    A_list[a] = A[a]


sub = len(B) - len(A)

result = []

cnt = 0

for i in range(len(A_list)):
    if A_list[i] == '':
        continue
    if A_list[i] != B_list[i]:
        cnt+=1
result.append(cnt)

for i in range(sub):
    
    for j in range(len(A)-1, -1, -1):
        A_list[j+i+1] = A[j]
        A_list[i] = ''
    cnt = 0
    
    for j in range(len(A_list)):
        if A_list[j] == '':
            continue
        if A_list[j] != B_list[j]:
            cnt+=1
    result.append(cnt)

print(min(result))
A, B = input().split()

A_list = ['' for _ in range(len(B))]
B_list = list(B)

A_lists = []

for a in range(len(A)):
    A_list[a] = A[a]


sub = len(B) - len(A)

result = []

cnt = 0

for i in range(len(A_list)):
    if A_list[i] == '':
        continue
    if A_list[i] != B_list[i]:
        cnt+=1
result.append(cnt)

for i in range(sub):
    
    for j in range(len(A)-1, -1, -1):
        A_list[j+i+1] = A[j]
        A_list[i] = ''
    cnt = 0
    
    for j in range(len(A_list)):
        if A_list[j] == '':
            continue
        if A_list[j] != B_list[j]:
            cnt+=1
    result.append(cnt)

print(min(result))
