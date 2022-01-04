N  = int(input())
Card = []

for i in range(1, N+1):
    Card.append(i)
#print(Card) #index N 이 제일 아래, index 0이 제일 위 1 2 3 4

result = []

while len(Card) != 1:
    #print(Card[0])
    del Card[0]
    #print(Card)
    Card.append(Card[0])
    #print(Card)
    del Card[0]
    #print(Card)

    result.append(Card[0])
#print(result)

print(1, end=' ')
for i in result:
    print(i, end=' ')
