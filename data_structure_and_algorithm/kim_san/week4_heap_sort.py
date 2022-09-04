def heapify(arr, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and arr[left_index] > arr[largest]:
        largest = left_index

    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)

def heap_sort(arr):
    length = len(arr)

    for i in range(length // 2 - 1, -1, -1):
        heapify(arr, i, length)

    for i in range(length - 1, 0 , -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr

list = [5,2,3,9,6,1,8,4,7]

print(heap_sort(list))

# 출처: https://my-devblog.tistory.com/38 
