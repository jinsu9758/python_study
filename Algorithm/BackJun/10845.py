N = int(input())
result = []
q = []

def push(num):
    q.append(num)

    
def front():
    if len(q) == 0:
        return -1
    else:
        return q[0]


    
def back():
    if len(q) == 0:
        return -1
    else:
        return q[-1]


def size():
    return len(q)


def empty():
    if len(q) == 0:
        return 1
    else:
        return 0

    
for i in range(N):
    
    cmd = input()
    
    if 'push' in cmd:
        cmd = cmd.split(' ')
        #print(cmd)
        num = cmd[1]
        num = int(num)
        push(num)
    
    elif cmd == 'front':
        result.append(front())
    
    elif cmd == 'back':
        result.append(back())
    
    elif cmd == 'size':
        result.append(size())
    
    elif cmd == 'empty':
        result.append(empty())
    
    elif cmd == 'pop':
        if len(q) == 0:
            result.append(-1)
        else:
            result.append(q.pop(0))

for i in result:
    print(i)
    
    