# 시간초과
'''
w, h = map(int, input().split()) # 좌표의 크기
p, q = map(int, input().split()) # 첫 시작점
time = int(input()) # 횟수

dx = 1
dy = 1
while time > 0:
    if p == 0 or p == w:
        if dx > 0:
            dx = -1
        else:
            dx = 1
    if q == 0 or q == h:
        if dy > 0:
            dy = -1
        else:
            dy = 1
    p = p + dx
    q = q + dy
    time -= 1
print(p , q)
'''

# 시간 줄이기
w, h = map(int, input().split()) # 좌표의 크기
p, q = map(int, input().split()) # 첫 시작점
time = int(input()) # 횟수

x = int((p + time) / w) #-> w를 몇번 움직였는지
# 축에 닿으면, x가 올라가는 원리
y = int((q+time) / h)


if x % 2 == 1: 
    p = w - ((p + time) % w)
else:
    p = (p + time) % w

if y % 2 == 1:
    q = h - ((q + time) % h)
else:
    q = (q + time) % h
    

print(p, q)