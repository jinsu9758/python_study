List = []
while True:
    Input_lists = list(map(int, input().split()))
    if Input_lists[0] == 0:
        break
    else:
        List.append(Input_lists)

#print(len(List)) #2

#for i in range(len(List)):

s = []

k = []

for i in range(len(List)):
    k.append(List[i][0])
    List[i].pop(0)

#print(k) #7, 8
#print(List) [[], []]


def dfs(start, L):
    if len(s) == 6:
        #print(s)
        for i in range(6):
            if i == 5:
                print(s[i])
                continue
            print(s[i], end=' ')
        return
    #for L in List:
    for index in range(start, len(L)):
        if L[index] not in s:
            s.append(L[index])
            dfs(index + 1, L)
            s.pop()

#dfs(0)

for i in range(len(List)):
    dfs(0, List[i])
    if i != len(List) - 1:
        print()
    