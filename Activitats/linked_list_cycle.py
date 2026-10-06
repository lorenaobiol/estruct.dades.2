class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def get_next(self):
        return self.next


def hasCycle(head: ListNode) -> bool:
    if head.get_next:
        return True
    else:
        return False
