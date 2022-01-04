cnt_card = [13, 13, 13, 13] #PKHT

my_card = input()

my_card_list = []
#print(len(my_card)) #12
for index in range(0, len(my_card), 3):
    my_card_list.append(my_card[index:index+3])

#print(my_card_list)

cnt = 0
for i in range(len(my_card_list)):
    for j in range(i+1, len(my_card_list)):
        if my_card_list[i] == my_card_list[j]:
            cnt+=1
if cnt>0:
    print("GRESKA")
else:
    for card in my_card_list:
        if card[0] == "P":
            cnt_card[0] -= 1
        elif card[0] == "K":
            cnt_card[1] -= 1
        elif card[0] == "H":
            cnt_card[2] -= 1
        elif card[0] == "T":
            cnt_card[3] -= 1
    print(cnt_card)
