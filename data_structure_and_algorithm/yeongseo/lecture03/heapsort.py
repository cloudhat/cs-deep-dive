
def max_heapify(arr, i): # 배열, 인덱스
    """
    O(log N) : 루트노드에서 시작할 경우 최대 Log n만큼 걸린다
    """

    if 2*i < len(arr):
        if arr[2*i] > arr[i]:
            largest = 2*i
        else:
            largest = i
    else:               # 단말 노드인 경우 끝내줘야 함
        return
    
    if 2*i + 1 < len(arr):
        if arr[2*i + 1] > arr[largest]:
            largest = 2*i + 1
    
    if largest != i: 
        tmp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = tmp
        max_heapify(arr, largest)


def build_max_heap(arr):
    """
    상위 노드로 갈수록
    1. 작업은 증가하고
    2. 노드는 적어진다

    n/4(1c) + n/8(2c) ..... + 1(log n c) [c는 상수]
   :n/4층.........................루트
   = c2^k(1/2^0 + 2/2^1 +...... (k+1)/2^k)
   = Σ[i= 0 ~ k] (i+1) / 2^ i 
   = 2.xxx
= O(N)
    """

    for i in range(len(arr)//2, -1, -1):
        max_heapify(arr,i)

def heapsort(arr):
    """
    N = len(arr)
    O(N log N + N) , 이때 N은 무시되므로
    O(N log N)
    """
    ans = []
    build_max_heap(arr)
    while arr:
        tmp = arr[-1]
        arr[-1] = arr[0]
        arr[0] = tmp
        pop = arr.pop()
        ans.append(pop)
        max_heapify(arr,0)
    
    return ans

print(heapsort([1,5,2,7,9,6,10,3,4,0]))