''' 틀렸음. 왜 틀렸을까?
N = int(input())
Input = [int(input()) for _ in range(N)]

tri = []

for i in Input:
    n = 1
    k = 0
    tri_list = []
    while k < i:
        k = n*(n+1)//2
        if k<i:
            tri_list.append(k)
            n += 1
    tri.append(tri_list)
#print("삼각수 리스트", tri)
    
def back(start, L, n):
    if len(stack) == 3:
        sum = 0
        index = 0
        for k in stack:
            sum += k
        if sum == Input[n]:
            result.append(1)
        return
    for j in range(start, len(L)):
        stack.append(L[j])
        back(j+1, L, n)
        stack.pop()

            
for n in range(len(tri)):
    start = 0
    result = []
    stack = []
    back(start, tri[n], n)
    if 1 in result:
        print(1)
    else:
        print(0)

'''


'''    틀렸음. 이거또한 왜 틀렸음?
import itertools

N = int(input())

Input = [int(input()) for _ in range(N)]

tri = []

for i in Input:
    n = 1
    k = 0
    tri_list = []
    while k < i:
        k = n*(n+1)//2
        if k<i:
            tri_list.append(k)
            n += 1
    tri.append(tri_list)

#print(tri)
n = 0
for j in tri:
    result = []
    c = itertools.combinations(j, 3)
    for L in list(c):
        sum = 0
        #print(L)
        for l in L:
            sum += l
            #print(sum)
        if sum == Input[n]:
            result.append(1)
    n += 1
    if 1 in result:
        print(1)
    elif 1 not in result:
        print(0)
'''




'''  다른사람이 푼거 아이디어 좋아보임.
triangle = [n*(n+1)//2 for n in range(1, 46)]
eureka = [0] * 1001

#미리 1000이하의 모든 유레카 수를 구한다
for i in triangle:
    for j in triangle:
        for k in triangle:
            if i+j+k <= 1000:
                eureka[i+j+k] = 1

T = int(input())
for _ in range(T):
    print(eureka[int(input())])
'''   


    

            
            
                
            
            


