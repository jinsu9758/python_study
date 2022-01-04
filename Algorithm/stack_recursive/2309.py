import itertools

sp = [int(input()) for _ in range(9)]

c = itertools.combinations(sp, 7)

#print(list(c))

result = []
for i in list(c):
    #print(i)
    sum = 0
    for j in i:
        sum += j
    if sum == 100:
        i = list(i)
        i.sort()
        '''
        #print(i)
        for k in i:
            print(k)
        '''
        result.append(i)
#print(result[0])
for k in result[0]:
    print(k)
        
