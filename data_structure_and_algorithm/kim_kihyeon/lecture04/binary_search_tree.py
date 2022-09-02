# 이진 탐색 트리
# 딕셔러니, 세트 등의 자료형에 쓰임
# 이진트리 + 속성

# 속성
# 특정 노드를 지정한 후 왼쪽 노드는 특정노드보다 작아야 하고 
# 오른쪽 노드는 특정 노드보다 커야 한다.

# 이진탐색 노드를 사용하면 데이터를 쉽게 찾을 수 있다.

# 완전 이진 트리라는 보장이 없기에
# 배열이나 파이썬 리스트로 구현하지 않는다.
# => 노드 클래스를 정의한 후 인스턴스를 생성한 한 후에 연결해 구현

# 삽입 시간 복잡도
# 최악의 경우 O(h+1) => O(h)
# 새로운 노드 생성 : O(1), 
# 루트 노드부터 비교하면서 저장위치 찾음 : O(h), 
# 찾은 위치에 새롭게 만든 노드 연결 : O(1)
# => O(1 + h + 1) = O(h)
class Node:
    """이진 탐색 트리 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None


def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None


    def insert(self, data):
        new_node = Node(data)  # 삽입할 데이터를 갖는 새 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        temp = self.root
        
        # 원하는 위치를 찾아간다
        while temp is not None:
            if data > temp.data:  # 삽입하려는 데이터가 현재 노드의 데이터보다 크다면
                if temp.right_child is None:
                    new_node.parent = temp
                    temp.right_child = new_node
                    return
                else:  # 삽입하려는 데이터가 현재 노드의 데이터보다 작다면
                    temp = temp.right_child
            else:  # 삽입하려는 데이터가 현재 노드 데이터보다 작다면
                # 왼쪽 자식이 없으면 새로운 노드를 현재 노드 왼쪽 자식으로 만듦
                if temp.left_child is None:
                    new_node.parent = temp
                    temp.left_child = new_node
                    return
                # 왼쪽 자식이 있다면 왼쪽 자식으로 간다
                else:
                    temp = temp.left_child
    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다


# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 이진 탐색 트리 출력
bst.print_sorted_tree()