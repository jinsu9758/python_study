m, s = map(int, input().split())
#print(m, s)

ntime = int(input())

if s+ntime < 60:
    print(m, s+ntime)
elif s+ntime >= 60:
    add_m = 0
    minute = s+ntime
    while minute >= 60:
        minute -= 60
        add_m += 1
    #print(m+add_m)
    print((m+add_m) % 24, minute)