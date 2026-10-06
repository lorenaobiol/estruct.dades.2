class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False
    
    primer = head             
    despues = head.next       
  
    while primer is not despues:
        
        if not despues or not despues.next:
            return False
        
        primer = primer.next
        despues = despues.next.next
        
    return True

