# 합병 정렬 Basic
# 1. Divide  : 리스트를 반으로 나눈다
# 2. Conquer : 왼쪽 리스트와 오른쪽 리스트를 각각 정렬한다
# 3. Combine : 정렬된 두 리스트를 하나의 정렬된 리스트로 합병한다


def merge(list1, list2):
    # list1, list2는 이미 정렬되어있음
    merged_list = []
    i = 0
    j = 0
    
    # list1과 list2를 돌면서 merged_list에 추가
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1
            
    # i가 len(list1)인 경우 list1이 소진된 것
    if  i == len(list1):
        merged_list.append(list2[j:])
    elif j == len(list2):
        merged_list.append(list1[i:])

    return merged_list


def merge_sort(my_list):

    # base case : 길이가 0 or 1인 경우 이미 정렬된 리스트
    if len(my_list) < 2:
        return my_list
    
    mid = len(my_list) //2
    
    left_half  = my_list[:mid]
    right_half = my_list[mid:] # mid+1로 착각
    
    # recursive case : merge의 파라미터로 넘겨주기
    return merge(merge_sort(left_half), merge_sort(right_half))
    
