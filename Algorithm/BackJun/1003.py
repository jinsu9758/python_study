T = int(input())

N_list = []

for i in range(T):
    N = int(input())
    N_list.append(N)
    
for i in N_list:
    zero = [1, 0]
    one = [0, 1]
    if i>=0 and i<=1:
        print(zero[i], one[i])
    elif i>1:
        for j in range(2, i+1):
            zero.append(zero[j-2] + zero[j-1])
            one.append(one[j-2] + one[j-1])
        #print(zero)
        #print(one)
        print(zero[i], one[i])