def merge(left, right): # O(left + right)
    l = 0
    r = 0
    new = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            new.append(left[l])
            l += 1
        else:
            new.append(right[r])
            r += 1
    
    if l < len(left):
        new.extend(left[l:])
    elif r < len(right):
        new.extend(right[r:])
    
    return new
    

def merge_sort(arr): 
    ''' 
    n = len(arr)    
    O(n) 작업(각 층에서의 merge)를 O(1 + log n)번 반복(나눠지는 계층 수)
    '''

    if len(arr) == 2: 
        return merge(arr[:1], arr[1:])
    elif len(arr) == 1:
        return arr
    
    else:
        return merge(merge_sort(arr[:len(arr)//2]),merge_sort(arr[len(arr)//2:])) 
    

print(merge_sort([5,9,6,2,8,7,7,2,6,1,4,3,10]))