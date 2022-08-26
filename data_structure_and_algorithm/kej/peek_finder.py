#1차원 극댓값 찾기
def peak_finder_1d(nums : list):
    
    if len(nums) == 0 :
        return None
    
    if len(nums) < 3 :
        return max(nums)
    
    # 인덱스의 중간값부터 시작해서 탐색한다고 가정
    if nums[len(nums)//2-1] > nums[len(nums)//2] :
        return peak_finder_1d(nums[:len(nums)//2])
        
    elif nums[len(nums)//2] < nums[len(nums)//2+1] :
        return peak_finder_1d(nums[(len(nums)//2)+1:])
    
    else :
        return nums[len(nums)//2]

#2차원 극댓값 찾기
def peak_finder_2d(matrix : list) -> int:
    #중간 행의 최대값을 찾은 후, 극댓값 비교. 
    mid_row     = matrix[len(matrix)//2]
    mid_row_max = max(mid_row)
    
    #mid_row_max의 인덱스 탐색
    idx = 0
    for index, value in enumerate(mid_row):
        if value == mid_row_max:
           idx = index
    
    if len(matrix) == 1:
        return max(matrix[0])
    
    if len(matrix) == 2:
        return max(matrix[0][idx], mid_row[mid_row_max])
    
    #mid_row의 전, 후 행의 idx값을 확인하여 극댓값 탐색
    if matrix[len(matrix)//2-1][idx] > mid_row_max:
        return peak_finder_2d(matrix[:len(matrix)//2])
    
    elif matrix[len(matrix)//2+1][idx] > mid_row_max:
        return peak_finder_2d(matrix[len(matrix)//2+1:])
    
    else:
        return mid_row_max