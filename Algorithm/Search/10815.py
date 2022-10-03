import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
#print(nums)
nums.sort()
#

M = int(sys.stdin.readline())
nums2 = list(map(int, sys.stdin.readline().split()))


for n in nums2:
    L = 0
    R = N - 1
    while L <= R:
        M = (L+R)//2
        if nums[M] < n:
            L = M + 1
        else:
            R = M - 1
    #print(L)
    if L<=N-1 and nums[L] == n:
        print(1, end=' ')
    else:
        print(0, end=' ')