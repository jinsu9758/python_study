def merge_sort(my_list):
    start = 0
    end = len(my_list) - 1
    if start == end: 
        return my_list
    mid = (start + end) // 2
    list1 = merge_sort(my_list[start: mid + 1])
    list2 = merge_sort(my_list[mid + 1: end + 1])
    return merge(list1, list2)

def merge(list1, list2):
    if len(list1) < 1 or len(list2) < 1:
        return list2 + list1
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
            
        else:
            merged_list.append(list1[i])
            i += 1
            
            
            
    if i < len(list1):
        merged_list += list1[i:]
        #merged_list += list2[j:]
    else: 
        #merged_list += list1[i:]
        merged_list += list2[j:]
            
    return merged_list

print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2,1]))