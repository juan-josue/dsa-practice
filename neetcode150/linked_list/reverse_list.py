# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        if not head:
            return head
        
        newHead = ListNode() # type: ignore
        curr = head
        while curr:
            temp = curr.next         # Temporarily save next node
            curr.next = newHead.next # Add the new linked list after curr
            newHead.next = curr      # Set curr as the new head
            curr = temp              # Update curr to the temp node
        return newHead.next