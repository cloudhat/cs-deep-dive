# l = left(i) : 왼쪽 자식 인덱스 i라면
# r = right(i): 오른쪽 자식 인덱스
# if (l <= heap-size(A) and A[l] > A[i]) : 만약 왼쪽 자식 인덱스가 힙 사이즈 보다 작거나 같고(힙 안에 존재), 왼쪽 자식노드의 값이 나(부모노드)보다 크면
# then largest = l else largest = i : 제일 큰 값이 왼쪽 자식노드이고, 아니면 제일 큰 값은 나다.(인덱스를 말함) 
# if (r <= heap-size(A) and A[r] > A[largest]) : 위의 내용을 오른쪽에 적용
# then largest = r 
# if largest != i : 만약 내 인덱스가 제일 먄
# then exchange A[i] and A[largest] 
# Max_Heapify(A, largest)

def max_heapify(A, largest):
    
    i = largest
    l = i*2
    r = l+1
    
    if l <= len(A) and A[l-1] > A[i-1]:
        largest = l

    if r <= len(A) and A[r-1] > A[largest-1]:
        largest = r
    
    if i != largest:
        A[i-1], A[largest-1] = A[largest-1], A[i-1]
        max_heapify(A, largest)
    
a = [16,4,10,14,7,9,3,2,8,1]

# Build_Max_Heap(A):
# for i=n/2 downto 1
# do Max_Heapify(A, i)

# 왜 n/2 부터 시작할까?
# 왜냐하면 요소 A[n/2 + 1 … n] 들이 트리의 모든 단말
# 2i > n, for i > n/2 + 1 

def built_max_heap(A):
    for i in range(len(A),1,-1):
        max_heapify(A,i)

print(built_max_heap(a))