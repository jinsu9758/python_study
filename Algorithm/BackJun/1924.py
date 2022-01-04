Months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Days = [30, 28, 31, 30, 31, 30, 31, 31, 30 , 31, 30, 31]
Yoil = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

x,y = map(int, input().split())

result_months = x - 1
result_days = y - 1

if result_months == 0:
    result = result_days
    print(Yoil[(result)%7])
elif result_months != 0:
    result = 0
    for i in range(1, result_months+1):
        result += Days[i-1]
    result += result_days
    #result += 1
    print(Yoil[(result+1)%7])