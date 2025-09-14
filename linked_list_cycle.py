# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    p1 = head
    p2 = head.next
    while p2 != None:
        if p1 is p2:
            return True
        else:
            p2 = p2.next 
            if p1 is p2:
                return True
            else:
                p2 = p2.next
                p1 = p1.next
    return False               
        
        