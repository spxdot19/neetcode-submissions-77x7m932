# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr is not None:
            nextN = curr.next
            curr.next = prev

            prev = curr
            curr = nextN
        
        return prev 

        # 0, 1, 2, 3
        # prev >> curr >> curr.next
        # 0    >> 1    >> None 
        # 1    >> 2    >> 0
        # 2    >> 3    >> 1
        # 3    >> None >> 2

