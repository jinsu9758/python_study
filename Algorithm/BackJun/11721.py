sen = input()


# print(sen, cnt)

a = 0
i = 10

print(sen[a:i])

while True:
    if len(sen[i:]) >= 10:
        a += 10
        i += 10
        print(sen[a:i])
    else:
        print(sen[i:])
        break   
    