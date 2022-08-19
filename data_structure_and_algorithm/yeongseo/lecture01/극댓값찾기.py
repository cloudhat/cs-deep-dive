def findlocal1D(arr):
    """
    - T(n) = T(n/2) + Θ(1), 이때 Θ(1)은 양쪽 확인하는 작업
    - base case : T(1) = Θ(1)
    => Θ(log2n)
    """
    if not arr:
        return None
    if len(arr) == 1: # arr의 길이 하나 되면 8라인에서 에러
        return arr[0]
    if len(arr) == 2: # [1,2]의 경우 이 조건 없다면 12라인 에러
        return max(arr)
   
    mid = len(arr) // 2
    if arr[mid] < arr[mid-1]:
        return findlocal1D(arr[:mid])
    elif arr[mid] < arr[mid+1]:
        return findlocal1D(arr[mid+1:])
    return arr[mid]


def findlocal2D(matrix):
    """
    n 개의 행, m개의 열
    T(n,m) = T(n/2,m) + Θ(m), 이때 Θ(m)은 행의 최댓값 확인하는 작업
    - base case : T(1,m) = Θ(m)
    => Θ(m log n)
    """
    n = len(matrix[0]) # 세로 길이 
    
    mid_row = matrix[n//2] # 가운데 행
    row_max = max(mid_row)

    idx = None 
    for i,v in enumerate(mid_row):
        if v == row_max:
            idx = i 
    
    if n == 1:
        return row_max
    if n == 2:
        return max(matrix[0][idx], row_max)
    
    if row_max < matrix[n//2 - 1][idx]: 
        return findlocal2D(matrix[:n//2]) # 행을 반으로 줄인다
    elif row_max < matrix[(n//2) + 1][idx]:
        return findlocal2D(matrix[(n//2)+1:])
    return row_max

print(findlocal2D(
    [
        [10,8,10,10],
        [14,13,12,11],
        [15,9,11,21],
        [16,17,19,20]
    ]
))