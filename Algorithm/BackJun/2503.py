List = []
for num in range(100, 999):
    num = str(num)
    if num[0]=='0' or num[1]=='0' or num[2]=='0' or num[0]==num[1] or num[0]==num[2] or num[1]==num[2]:
        pass
    else:
        List.append(num)

N = int(input())

for i in range(N):
    num2, strike, ball = map(int, input().split())
    num2 = str(num2)
    result = []
    for j in List:
        strike_cnt = 0
        ball_cnt = 0
        if j[0] == num2[0]:
            strike_cnt += 1
        if j[1] == num2[1]:
            strike_cnt += 1
        if j[2] == num2[2]:
            strike_cnt += 1
        if j[0] == num2[1]:
            ball_cnt += 1
        if j[0] == num2[2]:
            ball_cnt += 1
        if j[1] == num2[0]:
            ball_cnt += 1
        if j[1] == num2[2]:
            ball_cnt += 1
        if j[2] == num2[0]:
            ball_cnt += 1
        if j[2] == num2[1]:
            ball_cnt += 1
        if (strike_cnt == strike) and (ball_cnt == ball):
            result.append(j)
    List = result
print(len(List))