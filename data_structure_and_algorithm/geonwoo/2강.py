class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def delete(self, data):
        # 헤드값 없을때
        if self.head == '':
            print("해당값을 가진 노드가 없습니다.")
            return
 
        # 지우는값이 헤드값일때
        if self.head.data == data:
            tmp = self.head
            self.head = self.head.next
            del tmp
        else:
            # 지우는 값이 중간값일때
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next