N, M = map(int, input().split()) # N : 모니터 크기, M : 바구니 크기
apple = int(input())

start = 0 #바구니의 처음 인덱스
end = M #바구니의 끝 인덱스
cnt = 0 # 움직이는 횟수
move = 0

fall_index_list = []


# 떨어지는 인덱스 입력 리스트로 먼저 저장하기
for i in range(apple):
    fall_index = int(input())
    fall_index_list.append(fall_index)
    
#print(fall_index_list)

# 가만히 있어도 받아지는 경우, 오른쪽으로 움직어야 되는 경우, 왼쪽으로 움직여야 하는 경우

for i in range(apple):
    #가만히 있어도 받아지는 경우
    if start < fall_index_list[i] and end >= fall_index_list[i]:
        start = start
        end = end
    # 오른쪽으로 가야지 받아지는 경우
    elif end < fall_index_list[i]:
        move = fall_index_list[i] - end
        start += move
        end += move
        cnt += move
    # 왼쪽으로 가야지 받아지는 경우
    elif start >= fall_index_list[i]:
        move = start - fall_index_list[i] + 1
        start -= move
        end -= move
        cnt += move
print(cnt)