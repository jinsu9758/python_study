mush_list = []
for i in range(10):
    mush = int(input())
    mush_list.append(mush)

#print(mush_list)

sum2 = 0
index = 0
sub = 200

while index < 10:
    sum2 += mush_list[index]
    index += 1
    
    if sub >= abs(100-sum2):
        if 100-sum2 < 0:
            sub = abs(100-sum2)
            result = 100 + sub
        else: 
            sub = abs(100-sum2)
            result = 100-sub
    else:
        break
print(result)
