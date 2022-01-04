# 런타임 에러 94%? 울고싶다 8트만에 성공
bracket = list(input())
#print(bracket)

def is_avail(bracket):
    list_b =[]
    cnt = 0
    avail = 1
    for index in range(len(bracket)):
        if bracket[index]=='(' or bracket[index]==')' or bracket[index]=='[' or bracket[index]==']':
            pass
        else:
            return 0
        if bracket[index] == "(" or bracket[index] == "[":
            list_b.append(bracket[index])
        elif list_b and  bracket[index] == ")":
            if list_b[-1] == "(":
                list_b.pop()
            elif list_b[-1] == "[":
                avail = 0
                return avail
        elif list_b and  bracket[index] == "]":
            if list_b[-1]=="[":
                list_b.pop()
            elif list_b[-1] == "(":
                avail = 0
                return avail
        else:
            return 0
        #print(list_b)
    if len(list_b) == 0:
        avail = 1
        return avail
    else:
        avail = 0
        return avail


stack = []
if is_avail(bracket):
    tmp = 0
    #print("코드 짜야됨.")
    for i in range(len(bracket)):
        if bracket[i] == '(' or bracket[i] == '[':
            stack.append(bracket[i])
        elif bracket[i] == ')' and stack[-1] == "(":
            stack.pop()
            stack.append(2)
            if len(stack)>=2 and str(stack[-2]).isdecimal():
                tmp = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(tmp)
                tmp = 0
        elif bracket[i] == ']' and stack[-1] == "[":
            stack.pop()
            stack.append(3)
            if len(stack)>=2 and str(stack[-2]).isdecimal():
                tmp = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(tmp)
                tmp = 0
        elif bracket[i] == ')' and str(stack[-1]).isdecimal():
            stack.pop(-2)
            stack[-1] = stack[-1]*2
            if len(stack)>=2 and str(stack[-2]).isdecimal():
                tmp = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(tmp)
                tmp = 0
        elif bracket[i] == ']' and str(stack[-1]).isdecimal():
            stack.pop(-2)
            stack[-1] = stack[-1]*3
            if len(stack)>=2 and str(stack[-2]).isdecimal():
                tmp = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(tmp)
                tmp = 0
        #print(stack)
    s2 = 0
    for s in stack:
        s2 += s
    print(s2)
                
else:
    print(is_avail(bracket))

