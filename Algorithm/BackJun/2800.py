from itertools import combinations

sig = input()

def avail(sig):
    stack = []
    for s in sig:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if "(" in stack:
                stack.pop()
    
    if len(stack) != 0:
        return False
    else:
        return True

#부분집합 구현
def powerset(m_index):
    result = []

    for i in range(1, len(m_index)+1):
        c = combinations(m_index, i)
        result.extend(c)
    return result
    
# 출력 구현
def Print(result):
    #print(alive)
    result2 = []
    #print(result)
    for i in result:
        alive = [1 for _ in range(len(sig))]
        for j in i:
            for k in j:
                alive[k] = 0
        #print(alive)#이게 맞음
        a=""
        for s in range(len(sig)):
            if alive[s] == 1:
                a+=sig[s]
        result2.append(a)
    result2_set = set(result2)
    result2 = list(result2_set)
    result2.sort()
    #print(result2)
    return result2
                
'''                
l_index = []
r_index = []
m_index = []

if avail(sig):
    #괄호 짝짓기가 잘못되었음. (1)/(2)/(3)
    for index in range(len(sig)):
        if sig[index] == "(":
            l_index.append(index)
        elif sig[index] == ")":
            r_index.append(index)
    #print(l_index, r_index)#[0, 3, 6] [10, 11, 12]
    r_index = r_index[::-1]
    #print(l_index, r_index)#[0, 3, 6] [12, 11, 10]
    for index2 in range(len(l_index)):
        m_index.append([l_index[index2], r_index[index2]])
    #print(m_index)
    result = powerset(m_index)
    result2 = Print(result)
    for r in result2:
        print(r)
'''

index_stack = []
index_list = []

if avail(sig):
    for index in range(len(sig)):
        if sig[index]=="(":
            index_stack.append(index)
        elif sig[index]==")":
            if index_stack:
                top = index_stack.pop()
                index_list.append([top, index])
    result = powerset(index_list)
    result2 = Print(result)
    for r in result2:
        print(r)

