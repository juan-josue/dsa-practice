# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Len lst < 2
        if not head.next:
            return False

        slow, fast = head, head.next
        while fast and fast.next:
            # Check to see if fast has caught slow
            if fast == slow:
                return True
            
            # Advance fast and slow pointers
            fast = fast.next.next
            slow = slow.next
        return False