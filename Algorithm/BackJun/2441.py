height = int(input())

for i in range(height):
    for j in range(i):
        print(' ', end='')
    for k in range(height-i, 0, -1):
        print("*", end='')
    print()
        