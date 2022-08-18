
# 삽입 정렬
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i] 
        j = i-1
        while j >= 0 and lst[j] > key:  
            # key가 들어갈 공간 찾을때까지, 이전의 리스트를 한칸씩 오른쪽으로 밀어준다
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key  # 키가 들어갈 공간 찾았으니 삽입
    
    return lst

# print(insertion_sort([4,3,6,7,1,5,2]))


# 이진 삽입 정렬
def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] >= val:
            return start 
        else:
            return start + 1
    
    mid = (start + end) // 2
    if val < arr[mid]:
        return binary_search(arr, val, start, mid)
    
    elif val > arr[mid]:
        return binary_search(arr, val, mid+1, end)
    
    else:
        return mid
    
def binary_insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i] 
        # 여기에 이진탐색
        proper = binary_search(lst, key, 0, i)
        start = [] if proper == 0 else lst[:proper]
        middle = lst[proper:i]
        end = lst[i+1:]
        lst = start + [key] +  middle + end

    return lst


print(binary_insertion_sort([4,3,7,6,1,5,2]))