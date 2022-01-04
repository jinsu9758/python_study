A, B, C = map(int, input().split())

first1, first2 = map(int, input().split())
second1, second2 = map(int, input().split())
third1, third2 = map(int, input().split())

result  = [first1, first2, second1, second2, third1, third2]

max_input = max(result)

first_list = [0 for i in range(max_input-1)]
for i in range(first1-1, first2-1):
    first_list[i] = 1


second_list = [0 for i in range(max_input-1)]
for i in range(second1-1, second2-1):
    second_list[i] = 1

third_list = [0 for i in range(max_input-1)]
for i in range(third1-1, third2-1):
    third_list[i] = 1

#print(first_list)
#print(second_list)
#print(third_list)
cnt = 0
cnt_list = [0 for i in range(max_input-1)]
for i in range(max_input-1):
    if first_list[i] == 1:
        cnt += 1
    if second_list[i] == 1:
        cnt += 1
    if third_list[i] == 1:
        cnt += 1
    cnt_list[i] = cnt
    cnt = 0
    
#print(cnt_list)
sum = 0
for i in cnt_list:
    if i == 1:
        sum += A*i
    elif i == 2:
        sum += B*i
    elif i == 3:
        sum += C*i
        
print(sum)
