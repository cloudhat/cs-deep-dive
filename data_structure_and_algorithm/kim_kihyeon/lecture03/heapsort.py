# 힙
# 형태 속성 : 완전 이진트리
# 힙 속성   : 모든 노드의 데이터는 자식 노드들의 데이터보다 크거나 같다.

# 정렬 
# [4,1,6,2,8,5] => [1,24,5,6,8]
# 삽입정렬, 선택정렬, 퀵 정렬, 합병 정렬, 힙 정렬

# 힙 구현하기
# 자료형 리스트로 구현하기
# => 힙도 완전 이진트리이므로 동적 배열로 구현

# 힙의 만족 조건
# 1. 형태 속성 : 완전이진트리
# 2. 힙 속성   : 부모노드의 데이터 > 자식노드의 데이터

# heapify 알고리즘 (힙을 만족하도록 만드는 알고리즘)
# 최악의 경우 : O(lg(n)) // 높이에 비례한다.


def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index  = 2 * index
    right_child_index = 2 * index + 1

    # 코드를 쓰세요.
    largest = index
    
    
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index
    
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest) # 부모 노드와 최댓값을 가진 자식 노드의 위치를 변경
        heapify(tree, largest, tree_size)
        
# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1] # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))                      # 노드 2에 heapify 호출
print(tree) 



