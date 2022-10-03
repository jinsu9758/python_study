#퀵정렬 -> 메모리 초과
'''
N, K = map(int, input().split())

quick_list = list(map(int, input().split()))

#print(N, K, quick_list)

def quick_sort(quick_list):
    if len(quick_list) <= 1:
        return quick_list
    less_list, equal_list, greater_list = [], [], []
    pivot  = quick_list[len(quick_list)//2]
    for q in quick_list:
        if q < pivot:
            less_list.append(q)
        elif q > pivot:
            greater_list.append(q)
        else:
            equal_list.append(q)
    return quick_sort(less_list) + equal_list + quick_sort(greater_list)

result = quick_sort(quick_list)

print(result[K-1])
'''

#합병 정렬 -> 
'''
N, K = map(int, input().split())

merge_list = list(map(int, input().split()))

def Split(merge_list):
    start = 0
    end = len(merge_list) - 1
    mid= (start + end)//2

    if start == end:
        return merge_list
    
    list1 = Split(merge_list[start:mid+1])
    list2 = Split(merge_list[mid+1:end+1])
    #print(list1, list2)
    return Merge(list1, list2)

def Merge(list1, list2):
    #print(list1, list2)
    if len(list1)<1 or len(list2)<1:
        return list1 + list2

    merged_list = []

    i = 0
    j = 0

    while i<len(list1) and j<len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i+=1
    if i<len(list1):
        merged_list+=list1[i:]
    else:
        merged_list+=list2[j:]
    return merged_list

result = Split(merge_list)

print(result[K-1])
'''


