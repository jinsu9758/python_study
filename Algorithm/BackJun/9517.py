members=[1, 2, 3, 4, 5, 6, 7, 8]
second_list = []
correct_list = []

start = int(input())
start = start - 1 #index화 시켜주기

end = 210

quest = int(input())

second_sum = 0

for i in range(quest):
    second, answer = input().split()
    second = int(second)
    second_list.append(second)
    correct_list.append(answer)

for i in range(quest):
    second_sum += second_list[i]
    #print(start)
    if second_sum >= 210:
        print(members[start%8])
        break
    
    if correct_list[i] == "T":
        start += 1
    