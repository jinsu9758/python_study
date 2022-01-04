L, C = map(int, input().split())

alp = list(input().split())
alp.sort()
#print(L, C, alp)
stack = []
stack2 = []

def back(start):
    if len(stack) == L:
        #print(stack)
        stack2.append(''.join(stack))
        #print(type(stack))
        #stack2.append(stack) #이거는 대체 왜 안되는 걸까?
        return
    for i in range(start, C):
        if alp[i] not in stack:
            stack.append(alp[i])
            back(i+1)
            stack.pop()

back(0)
#print(stack2)
#최소 1개의 모음, 최소 2개의 자음.

vow = 'aeiou'

for i in stack2:
    cnt1 = 0
    cnt2 = 0
    for j in i:
        if j in vow:
            cnt1 += 1
        if j not in vow:
            cnt2 += 1
    if cnt1>=1 and cnt2>=2:
        print(i)
