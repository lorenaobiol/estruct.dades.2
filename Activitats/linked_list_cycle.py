class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False
    cicle=False
    despues=head.next
    primer=head
    while cicle==False:
        if despues != primer:
            despues=despues.next
            primer=primer.next.next
            if not despues or not despues.next:
                cicle=True
                return False
        else:
            cicle=True
    return True

