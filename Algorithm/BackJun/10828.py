stack = []
cmd_list = []

cnt = int(input())

for i in range(cnt):
    cmd = input()
    cmd_list.append(cmd)

#print(cmd_list)

def push(num):
    stack.append(num)
    
def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0
    
def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[len(stack) - 1]

for j in cmd_list:
    if 'push' in j:
        j = j.split(' ')
        num = j[1]
        num = int(num)
        #print(num)
        push(num)
    elif 'pop' == j:
        print(pop())
    
    elif 'size' == j:
        print(len(stack))
    
    elif 'empty' == j:
        print(empty())
    
    elif 'top' == j:
        print(top())