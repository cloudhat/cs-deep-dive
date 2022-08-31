class Node:
    def __init__(self,val):
        self.val    = val
        self.left   = None
        self.right  = None
        self.parent = None # 삭제를 위해 필요함 


class BST():  
    def __init__(self):
        self.root = None

    def bst_insert(self, root,value):
        if not root: # bst의 시작
            root = Node(value)
            return root

        if value == root.val: # 키가 같은 노드는 복수로 존재하지 않는다
            return 
        
        if value < root.val:
            if not root.left:
                root.left = Node(value)
                root.left.parent = root
            else:
                self.bst_insert(root.left, value)        
        else:
            if not root.right:
                root.right = Node(value)
                root.right.parent = root
            else:
                self.bst_insert(root.right, value) 

    def bst_find(self, root,value):
        if not root:
            return False

        if value == root.val:
            return True
        
        if value < root.val:
            return self.bst_find(root.left, value)
        
        if value > root.val:
            return self.bst_find(root.right, value)
    
    def bst_delete(self, root, value):
        if not root:
            return False

        if value < root.val:
            self.bst_delete(root.left, value)
        elif value > root.val:
            self.bst_delete(root.right, value)
        
        else: # value = root.val

            #자식 노드가 없는 노드 삭제
            if not root.left and not root.right: 
                if root.parent.left == root:
                    root.parent.left  = None
                else:
                    root.parent.right = None
            
            # 왼쪽 자식만 있는 노드 삭제
            elif root.left and not root.right:
                if root.parent.left  == root:
                    root.parent.left = root.left
                else:
                    root.parent.right = root.left
                
            # 오른쪽 자식만 있는 노드 삭제
            elif root.right and not root.left:
                if root.parent.left  == root:
                    root.parent.left = root.right
                else:
                    root.parent.right = root.right

            # 두 자식 모두 있는 노드 삭제
            else:
            # 왼쪽 트리에서 대체할 노드(값이 가장 큰 노드)를 찾은 이후, 이를 삭제할 노드와 바꾼다
                max_left = root.left
                while max_left.right:
                    max_left= max_left.right
                
                root.val = max_left.val

            # 옮긴 노드는 삭제한다
                # 1. 옮긴 노드의 왼쪽 자식이 없다
                if not max_left.left:
                    if max_left.parent.left == max_left:
                        max_left.parent.left = None
                    else:
                        max_left.parent.right = None

                
                # 2. 옮긴 노드의 왼쪽 자식이 있다
                elif max_left.left:
                    if max_left.parent.left == max_left:
                        max_left.parent.left = max_left.left
                    else:
                        max_left.parent.right = max_left.left
             
                


    def print_inorder(self, root):

        if root.left is not None: # root 왼쪽모두 출력
            self.print_inorder(root.left)
        print(root.val, end= ' ')          # root 출력
        if root.right is not None: # root 오른쪽 
            self.print_inorder(root.right)

root = BST().bst_insert(None,4)
BST().bst_insert(root,2)
BST().bst_insert(root,7)
BST().bst_insert(root,10)

BST().bst_insert(root,3)
BST().bst_insert(root,1)
BST().bst_insert(root,9)
BST().bst_insert(root,6)
print(BST().bst_find(root,6))
BST().bst_delete(root,7)


BST().print_inorder(root)




