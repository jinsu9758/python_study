import sys

def calc_len():
    _min = abs(ax-bx) + abs(ay-by)
    for i in range(2):
        for j in range(2):
            length = calc(A_cases[i][0], A_cases[i][1], B_cases[j][0], B_cases[j][1])
            print(length)
            if i==0 and j==0:
                length += (abs(ay-(R-P*ax)/Q) + abs(by-(R-P*bx)/Q))
            elif i==0 and j==1:
                length += (abs(ay-(R-P*ax)/Q) + abs((R-Q*bx)/P-bx))
            elif i==1 and j==0:
                length += (abs(ax-(R-Q*ay)/P) + abs(by-(R-P*bx)/Q))
            elif i==1 and j==1:
                length += (abs(ax-(R-Q*ay)/P) + abs((R-Q*by)/P-bx))
            if _min >= length:
                _min = length
    return _min


def calc(a_x, a_y, b_x, b_y):
    return ((a_x - b_x)**2 + (a_y - b_y)**2)**0.5
    

_input = sys.stdin.readline().split()

ax = int(_input[0])
ay = int(_input[1])
bx = int(_input[2])
by = int(_input[3])

P = float(_input[4])
Q = float(_input[5])
R = float(_input[6])

A_cases = [[ax, (R-P*ax)/Q], [(R-Q*ay)/P, ay]]
B_cases = [[bx, (R-P*bx)/Q], [(R-Q*by)/P, by]]

result = calc_len()
print(result)
