from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = last = ListNode()

        # Append lowest valued node to the new list until the end of a list is reached
        while list1 and list2:
            if list1.val < list2.val:
                last.next = list1
                list1 = list1.next
            else:
                last.next = list2
                list2 = list2.next
            last = last.next

        # Either list1 or list2 are empty, add remaining values to new list
        last.next = list1 if list1 else list2
            
        return first.next