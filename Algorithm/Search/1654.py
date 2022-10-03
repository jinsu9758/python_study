K, N = map(int, input().split())

lan_list = list(int(input()) for _ in range(K))

lan_list.sort()

#print(K, N, lan_list)

left = 1 # 0이면 안됨. (0+1)//2 -> 0 반복문에서 값/0이 되어버림.
right = max(lan_list)

while left <= right:
    middle = (left+right)//2
    lan_cnt = 0
    for l in lan_list:
        lan_cnt += l // middle
    if lan_cnt < N: #  middle이 크다는 소리.
        right = middle - 1
    elif lan_cnt >= N: # middle 이 작다는 소리
        left = middle + 1
print(right)
        
