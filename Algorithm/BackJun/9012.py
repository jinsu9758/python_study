N = int(input())
result = []

for i in range(N):
    temp = True
    s = []
    sen = list(input())
    #print(sen)
    for j in sen:
        if j == '(':
            s.append(1) # 왼쪽괄호는 숫자 1 집어넣기
        elif j == ')':
            if len(s) == 0:
                temp = False
            else:
                s.pop() # 오른쪽 괄호는 pop
    if len(s) == 0 and temp:
        result.append("YES")
    else:
        result.append("NO")

        
for i in result:
    print(i)
#print(s)
        
    