class ListNode:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        if index >= self.size:
            return -1
        node = self.head
        for i in range(index + 1):
            node = node.next
        return node.value

        
    def insertHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = self.head
        for i in range(self.size):
            node = node.next
        node.next = ListNode(val)
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        node = self.head
        for i in range(index):
            node = node.next
        node.next = node.next.next
        self.size -= 1
        return True
        

    def getValues(self) -> List[int]:
        lst = []
        node = self.head
        for i in range(self.size):
            node = node.next
            lst.append(node.value)
        return lst

        
