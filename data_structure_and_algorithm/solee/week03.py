# 그 루트의 서브 트리에서 힙 특성을 위반한 걸 한 가지 고친다.
def max_heapify(heap, i):
    left      = 2*i
    right     = 2*i+1
    largest   = i

    if left <= len(heap) and heap[left-1] > heap[i-1]:
        largest = left

    if right <= len(heap) and heap[right-1] > heap[largest-1]:
        largest = right
    
    if largest != i:
        heap[i-1], heap[largest-1] = heap[largest-1], heap[i-1]
        max_heapify(heap, largest)
    
# 정렬 되지 않은 배열로부터 최대-힙을 만든다.
def build_max_heap(heap):
    i = len(heap)//2
    for num in range(i, 0, -1):
        max_heapify(heap, num)

a = [16,4,10,14,7,9,3,2,8,1]
# max_heapify(a, 2)
build_max_heap(a)
print(a)