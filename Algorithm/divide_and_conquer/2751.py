# 퀵 정렬 -> 메모리 초과
'''
N = int(input())

quick_list = [int(input()) for _ in range(N)]

#print(N, quick_list)

def quick_sort(quick_list):
    if len(quick_list) <= 1:
        return quick_list

    pivot = quick_list[len(quick_list)//2]

    less_arr, equal_arr, more_arr = [], [], []

    for q in quick_list:
        if pivot < q:
            more_arr.append(q)
        elif pivot > q:
            less_arr.append(q)
        else:
            equal_arr.append(q)
    return quick_sort(less_arr) + equal_arr + quick_sort(more_arr)

result = quick_sort(quick_list)

for i in result:
    print(i)
'''

# 병합정렬
'''
N = int(input())

quick_list = [int(input()) for _ in range(N)]

def Split(quick_list):
    start = 0
    end = len(quick_list) - 1
    mid = (start + end)//2

    if start == end:
        return quick_list

    list1 = Split(quick_list[start:mid+1])
    list2 = Split(quick_list[mid+1:end+1])

    return Merge(list1, list2)


def Merge(list1, list2):
    if len(list1) < 1 or len(list1) < 1:
        return list1 + list2

    merged_list = []

    i = 0
    j = 0

    while i<len(list1) and j<len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i+=1
        else:
            merged_list.append(list2[j])
            j+=1
    if i<len(list1):
        merged_list += list1[i:]
    else:
        merged_list += list2[j:]
    return merged_list

result = Split(quick_list)

#print(result)
for r in result:
    print(r)
'''