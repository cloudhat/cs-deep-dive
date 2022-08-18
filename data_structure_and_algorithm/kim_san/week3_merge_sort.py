def merge_sort(array):

    if len(array)<2:
        return array

    mid_index=len(array)//2

    low_array=merge_sort(array[:mid_index])
    high_array=merge_sort(array[mid_index:])

    merged_array=[]
    low_array_index=high_array_index=0
    while low_array_index<len(low_array) and high_array_index<len(high_array):
        if low_array[low_array_index]<high_array[high_array_index]:
            merged_array.append(low_array[low_array_index])
            low_array_index+=1
        else :
            merged_array.append(high_array[high_array_index])

    merged_array.append(low_array[low_array_index:])
    merged_array.append(high_array[high_array_index:])

    return merged_array


array=[6, 5, 3, 1, 8, 7, 2, 4]
print("결과 : ", merge_sort(array))
    