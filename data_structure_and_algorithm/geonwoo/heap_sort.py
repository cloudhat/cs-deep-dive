def heapify(arr, index, heap_size):
    largest = index
    left = index * 2 + 1    
    right = index * 2 + 2   
    
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)
