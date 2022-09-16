class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 #탐색
class BinarySearchTree:
    def __init__(self, val):
        self.root = TreeNode(val)
        
        def find(self, val):
            if self.find_node(self.root, val):
            return True # 노드를 반환 받으면 True
        else:
            return False # 없으면 False
 
    def _find_node(self, cur, val):
        if not cur:
            return False # 마지막 리프노드까지 탐색해도 없으니 False
        if cur.val == val:
            return cur # 값을 발견하면 노드 반환
        if cur.val > val: # 커서의 값이 더 크면 좌측 탐색
            return self.find_node(cur.left, val)
        if cur.val < val: # 커서의 값이 더 작으면 우측 탐색
            return self._find_node(cur.right, val)
#삽입  
    def insert(self, val):
            self._insert_Node(self.root, val)
    
    def _insert_node(self, cur, val):
        if val <= cur.val:
            if cur.left:
                self._insert_node(cur.left, val)
            else:
                cur.left = TreeNode(val)
        elif val > cur.val:
            if cur.right:
                self._insert_node(cur.right, val)
            else:
                cur.right = TreeNode(val)
