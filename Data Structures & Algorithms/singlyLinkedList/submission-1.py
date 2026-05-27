class LinkNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = LinkNode(-1)
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr:
            return curr.val
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = LinkNode(val, self.head.next)
        self.head.next = new_node



    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = LinkNode(val)

    def remove(self, index: int) -> bool:
        prev = self.head
        i = 0
        while prev.next and i < index:
            prev = prev.next
            i += 1
        if prev.next:
            prev.next = prev.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next
        while curr:
            result.append(curr.val)
            curr = curr.next 
        return result
        
