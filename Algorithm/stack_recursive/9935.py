sen = input()
boom = input()
#print(sen, boom)

stack = []
l = len(boom) #2

for i in sen:
    stack.append(i)
    #print(stack)
    if stack[-1] == boom[-1]:
        #print(stack[(-1*l):], boom, stack[(-1*l):] == boom)
        if len(stack)>=l and ''.join(stack[(-1*l):]) == boom:
            #print(stack[-1*(1+l):-1])
            del stack[(-1*l):]
            #print(stack)
if len(stack) > 0:
    print(''.join(stack))
else:
    print('FRULA')
