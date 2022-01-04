cnt = int(input())

stack = []
result_list = []
sign = []

for i in range(cnt):
    Input = int(input())
    result_list.append(Input)

index = 0
start = 1


num = 1

use = True
for i in range(cnt):
    while num <= result_list[i]: #핵심
        stack.append(num)
        sign.append('+')
        num += 1    #핵심
    if stack[-1] == result_list[i]:
        stack.pop()
        sign.append('-')
    else:
        use = False
    
if use:
    for i in range(len(sign)):
        print(sign[i])
else:
    print("NO") 