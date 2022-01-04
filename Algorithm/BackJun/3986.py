N = int(input())

alp = [list(input()) for _ in range(N)]

success = 0

for a in alp:
    stack = []
    for l in a:
        if len(stack)==0:
            stack.append(l)
        elif stack[-1] == l:
            stack.pop()
        elif stack[-1] != l:
            stack.append(l)
    if len(stack)==0:
        success += 1
print(success)
        
        