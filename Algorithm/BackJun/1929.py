# 시간 초과
# a, b = map(int, input().split())

# result = []

# for i in range(a, b+1):
#     for j in range(2, i):
#         if i%j == 0:
#             break
#         elif j==i-1:
#             result.append(i)

# for k in result:
#     print(k)




#에라토스테네스의 체  -> 시간 초과?
# def sosu(n):
#     result = []
#     for i in n:
#         for j in range(2, i):
#             if i%j == 0:
#                 break
#             elif j==i-1:
#                 result.append(i)
#     return result        
    


# a, b = map(int, input().split())

# List = []

# for i in range(a, b+1):
#     List.append(i)
#     if i%2 == 0 and i!=2:
#         List.remove(i)
#     if i==1:
#         List.remove(i)

        
# sosu_list = sosu(List)


# for j in List:
#     for k in sosu_list:
#         if j%k==0 and j!=k:
#             try:
#                 List.remove(j)
#             except:
#                 pass


# for l in List:
#     print(l)




# 제곱근 사용하기
# 약수가 있는 숫자일 경우, sqrt(n) 까지만 확인하면, 약수의 유무를 파악할 수 있다.

import math as m

a, b = map(int, input().split())

def sosu(i):
    if i == 1:
        return False
    else:
        for j in range(2, int(m.sqrt(i))+1):
            if i%j == 0:
                return False
        return True
            
        

for i in range(a, b+1):
    if sosu(i):
        print(i)

        

            





















    

