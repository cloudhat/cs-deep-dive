# 노드 생성
class Node:
    def __init__(self, val:float) -> None:
        self.key    = val
        self.left   = None
        self.right  = None

class BinarySearchTree():
    # 루트노드 초기화
    def __init__(self, root:Node)->None:
        self.root = root
    
    # 노드 삽입
    def insert(self, val:float):
        self.current_node = self.root
        
        while True:
            if val == self.current_node.val:
                break
            
            elif val < self.current_node.val:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(val)
                    break
                
            else: 
                if self.current_node.right != None:
                    self.current_node.right = self.current_node.right
                    
                else:
                    self.current_node.right = Node(val)
                    break
        
    # find(val)
    def search(self, val):
        self.current_node = self.root
        while self.current_node:
            if self.current_node.val == val:
                return True
            elif val < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right 
                
# next-larger(x)
# Rank(t)