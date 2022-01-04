M = int(input())
M_list = list(map(int, input().split()))
M_list.sort()

N = int(input())
N_list = list(map(int, input().split()))

def half_det(i, start, end):
    n = (start + end) // 2

    if start > end:
        print(0)
        return 0

    if i > M_list[n] and n < M-1:
        start = n + 1
        half_det(i, start, end)
    elif i < M_list[n]:
        end = n -1
        half_det(i, start, end)
    elif M_list[n] == i:
        print(1)
    else:
        print(0)
        
start = 0
end = M-1

for i in N_list:
    half_det(i, start, end)
    
