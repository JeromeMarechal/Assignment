# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        length = 0
        current = head
        while current != None:
            length += 1
            current = current.next
            
            
        result = 0
        while head != None:
            result = head.val * 2**(length - 1) + result
            length -= 1
            head = head.next
            
        return result      