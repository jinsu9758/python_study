alp = list(input())
alp.sort()

alp_cnt = [0 for _ in range(26)]

cnt = 0
for al in alp:
    alp_cnt[ord(al)-65] += 1

for i in range(26):
    if alp_cnt[i]%2 == 1:
        cnt+=1

if cnt > 1:
    print("I'm Sorry Hansoo")
elif cnt == 0:
    result = ""
    for al in alp:
        if alp_cnt[ord(al)-65] > 0 and al not in result:
            for i in range(alp_cnt[ord(al)-65]//2):
                result+=al
    result+=result[::-1]
    print(result)
elif cnt == 1:
    result = ""
    result2 = ""
    for al in alp:
        if alp_cnt[ord(al)-65]%2 ==1:
            middleware = al
    
    for al in alp:
        if alp_cnt[ord(al)-65] > 0 and al not in result:
            for i in range(alp_cnt[ord(al)-65]//2):
                result += al
                result2 = result
    result += middleware
    result += result2[::-1]
    print(result)

