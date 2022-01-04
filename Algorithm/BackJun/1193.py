# 분자 분모의 배열을 직접 만들어서 입력 값의 index 배열의 값을 뽑아오기

num = int(input())

num2 = num # 값 복사
cnt = 1
cnt2 = 1


while(num>0):
    num = num - cnt
    cnt += 1
    cnt2 += 1
cnt -= 1



def cal_index(cnt):
    sum = 0
    for i in range(1, cnt):
        sum += i
    return sum

        

# cnt가 짝수이냐 홀수이냐에 따라 들어가는 값이 달라짐 (분자)
if cnt % 2 == 0:
    son = [j for j in range(1, cnt2)][num2 - cal_index(cnt) -1]
elif cnt % 2 == 1:
    son = [j for j in range(cnt2-1, 0, -1)][num2 - cal_index(cnt) -1]

    
# cnt가 짝수이냐 홀수이냐에 따라 들어가는 값이 달라짐 (분모)
if cnt % 2 == 0:
    par = [j for j in range(cnt2-1, 0, -1)][num2 - cal_index(cnt) -1]
elif cnt % 2 == 1:
    par = [j for j in range(1, cnt2)][num2 - cal_index(cnt) -1]


print("{}/{}".format(son, par))
