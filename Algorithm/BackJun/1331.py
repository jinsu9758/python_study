row = [i for i in range(1, 7)]
col = [chr(j) for j in range(ord('A'), ord('F')+1)]
#print(row)
#print(col)

all_node = []
for j in row:
    for i in col:
        all_node.append(i+str(j))
#print(all_node)


dx = [2, 2, -2, -2, -1, 1, -1, 1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

node_list = []
visit_node = []

cnt2 = 0
for i in range(36):
    node = input()
    node_list.append(node)
    if node not in visit_node and node in all_node:
        visit_node.append(node)
    else:
        cnt2 += 1

#print(str(node_list[0])[0]) #A

cnt = 0
for index in range(len(node_list)):
    alp1 = node_list[index][0]
    alp2 = node_list[index][1]
    #print(type(alp1), type(alp2))
    poss_visit_node = []
    for i in range(8): #8
        if 65<=ord(alp1)+dx[i]<=70 and 49<=ord(alp2)+dy[i]<=54:
            poss_node = chr(ord(alp1)+dx[i]) + chr(ord(alp2)+dy[i])
            #print(poss_node)
            poss_visit_node.append(poss_node)
    #print(node_list[index+1], poss_visit_node)
    if index<=34 and node_list[index+1] not in poss_visit_node:
        #print(visit_node)
        cnt += 1

#print(node_list[35], node_list[0])
cnt3 = 0
poss_node2 = []
poss_visit_node2 = []
a, b = node_list[35][0], node_list[35][1]
#print(a, b)
for j in range(8):
    if 65<=ord(a)+dx[j]<=70 and 49<=ord(b)+dy[j]<=54:
        poss_node2 = chr(ord(a)+dx[j]) + chr(ord(b)+dy[j])
        #print(poss_node2)
        poss_visit_node2.append(poss_node2)

#print(node_list[0], poss_visit_node2)

if node_list[0] not in poss_visit_node2:
    cnt3 += 1

#print(cnt, cnt2, cnt3)    
if cnt+cnt2+cnt3 > 0:
    print("Invalid")
else:
    print("Valid")
