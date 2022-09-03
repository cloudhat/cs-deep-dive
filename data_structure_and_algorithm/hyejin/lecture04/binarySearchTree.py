
class Node:
	# 이진 탐색 트리 노드 클래스
	def __init__(self, data):
		self.data = data
		self.parent = None # 노드 부모의 레퍼런스
		self.left_child = None
		selt.right_child = None

# 노드 인스턴스 생성
node_0 = Node(5)
node_1 = Node(3)
node_2 = Node(7)

# node_0을 루트 노드로 갖는 이진 탐색 트리
node_0.left_child = node_1
node_0.right_child = node_2

node_1.parent = node_0
node_2.parent = node_0

def print_inorder(node):
    # 주어진 노드를 in-order로 출력해주는 함수
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)

class BinarySearchTree:
	# 이진 탐색 트리 클래스
	def __init__(self):
		self.root = None

	def print_sorted_tree(self):
	  # 이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드
	  print_inorder(self.root)  # root 노드를 in-order로 출력한다
	

# 비어 있는 이진 탐색 트리 생성		
bst = BinarySearchTree()