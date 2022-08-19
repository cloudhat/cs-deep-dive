# 1차원 극댓값
def peak_find_1d(nums):
    
    if not nums:
        return None
    if len(nums) < 2:
        return max(nums)
    
    mid = len(nums) // 2
    
    if nums[mid - 1] > nums[mid]:
        return peak_find_1d(nums[:mid])
    elif nums[mid - 1] < nums[mid]:
        return peak_find_1d(nums[mid+1:])
    else:
        return nums[mid]
    

# 2차원 극댓값
'''
m는 여기서 mid_row
중앙 열 j = matrix/2을 선택한다.
(i, j)에서 j열의 최댓값을 찾는다.

(n, m − 1), (n, m), (n, m + 1)를 비교한다.
(n, m − 1) > (n, m)이면 왼쪽 열을 선택한다.
오른쪽도 똑같이 진행한다.

두 조건 모두 만족하지 않으면, (n, m)가 2차원 극댓값이다.
열 개수가 절반으로 줄어든 새로운 문제를 푼다.
열이 1개 남으면, 최댓값을 찾고 끝난다.
'''
def peak_find_2d(matrix):
    mid_row     = matrix[len(matrix)//2] # 중앙 열 j = matrix/2을 선택한다.
    max_mid_row = max(mid_row) # (i, j)에서 "j"열의 최댓값을 찾는다.

    idx = 0
    for index, value in enumerate(mid_row):
        if value == max_mid_row:
            idx = index

    # (n, m − 1), (n, m), (n, m + 1)를 비교한다.
    # 만약 matrix의 길이가 1개 => 열이 1개 남으면, 최댓값은 matrix[0]
    if len(matrix) == 1:
        return max(matrix[0])
    
    # 혹은 2개일 경우
    elif len(matrix) ==2:
        return max(matrix[0][idx], mid_row[max_mid_row])
    
    # mid_row 전후 탐색
    # (n, m − 1) > (n, m)이면 왼쪽 열을 선택한다.
    if matrix[len(matrix)//2-1][idx] > max_mid_row:
        # 열 개수가 절반으로 줄어든 새로운 문제를 푼다.
        return peak_find_2d(matrix[:len(matrix)//2])

    # mid_row 전후 탐색
    # (n, m − 1) < (n, m)이면 오른쪽 열을 선택한다.    
    elif matrix[len(matrix)//2+1][idx] < max_mid_row:
        # 열 개수가 절반으로 줄어든 새로운 문제를 푼다.
        return peak_find_2d(matrix[len(matrix)//2+1])
    
    else:
        return max_mid_row