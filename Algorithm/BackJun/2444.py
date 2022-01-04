num = int(input())

for i in range(num):
    for j in range(num-i, 1, -1):
        print(' ', end='')
    for k in range(1, 2*i+2):
        print("*", end='')
    print()

for i in range(num-1):
    for j in range(1, i+2):
        print(' ', end='')
    for k in range(2*(num-1)-(2*i+1) , 0, -1):
        print("*", end='')
    print()
    