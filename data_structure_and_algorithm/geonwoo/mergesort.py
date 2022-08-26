def merge_sort(a):
    def sort(unsorted_list):
        if len(unsorted_list) <= 1:
            return
        # 두개의 리스트로 분할. 아래에서 재귀적으로 시행
        mid = len(unsorted_list) // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right)
        
    def merge(left, right):
        i = 0
        j = 0
        k = 0
        while (i < len(left)) and (j < len(right)):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
                k+= 1
            else:
                a[k] = right[j]
                j += 1
                k+= 1
        # 남은 데이터 삽입
        while i < len(left):
            a[k] = left[i]
            i += 1
            k+= 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k+= 1
        print(a)
    sort(a)
array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
merge_sort(array)