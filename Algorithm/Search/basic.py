# https://www.acmicpc.net/blog/view/109
#  이분탐색 헷갈리지 않게 구현하기
'''
반복 조건문 -> left + 1 < right
구한 경계에서 답이 left인지 right인지 생각해보고 출력

* 탐색이 끝나면 left, right는 답이 바뀌는 경계에 위치해있음.
문제 답의 분포 : F~T
정답이 가장 큰 F이면, left
정답이 가장 작은 T이면, right
'''

# 예시 한번 풀어보기
# 백준 1920

import sys
N = int(sys.stdin.readline())
num1 = list(map(int, sys.stdin.readline().split()))
num1.sort() #1 2 3 4 5

M = int(sys.stdin.readline())
num2 = list(map(int, sys.stdin.readline().split()))

for n in num2:
    left = 0
    right = N
    while left + 1 < right:
        middle = (left + right)//2
        #print(left, right)
        if num1[middle] > n:
            right = middle
        else:
            left = middle
    #print(left)
    if n == num1[left]:
        print(1)
    else:
        print(0)
    

'''
5
4 1 5 2 3
5
1 3 7 9 5

1
1
0
0
1

'''


