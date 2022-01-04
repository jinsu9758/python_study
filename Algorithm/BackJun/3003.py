result = []
chess = [1, 1, 2, 2, 2, 8]
a, b, c, d, e, f = map(int, input().split())
Input = []
Input.append(a)
Input.append(b)
Input.append(c)
Input.append(d)
Input.append(e)
Input.append(f)

for i in range(6):
    result.append(chess[i] - Input[i])

for i in result:
    print(i, end=' ')
