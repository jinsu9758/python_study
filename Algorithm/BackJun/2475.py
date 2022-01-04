num = list(map(int, input().split()))
#print(num)

sum = 0
for i in range(len(num)):
    sum += pow(num[i],2)
print(sum%10)
    