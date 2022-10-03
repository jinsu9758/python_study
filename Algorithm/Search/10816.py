# 시간 초과
'''
import copy
N = int(input())
num_card = list(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))


num_card.sort()
num_card2 = copy.deepcopy(num_card)

#print(target)

#print(num_card)

cnt_list = [0 for _ in range(max(target)+1)]

for t in target:
    num_card = copy.deepcopy(num_card2)
    #print(num_card)
    left = 0
    right = len(num_card)-1
    while left<=right:
        middle = (left+right)//2
        #print(left, right, middle)
        if t < num_card[middle]:
            right = middle -1
        elif t > num_card[middle]:
            left = middle+1
        elif t == num_card[middle]:
            num_card.pop(middle)
            right -= 1
            cnt_list[t] += 1
            #print(cnt_list)
#print(*cnt_list)

for t in target:
    print(cnt_list[t], end=' ')
'''            
            
N = int(input())
num_card = list(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))

dic = dict()
for n in num_card:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
#print(dic)

for t in target:
    if t in dic:
        print(dic[t], end=' ')
    else:
        print(0, end=' ')
    


