# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        hl,hg = ListNode(),ListNode()
        nl,ng = hl,hg
        while head:
            if head.val < x:
                nl.next = head
                nl = nl.next
            else:
                ng.next = head
                ng = ng.next
            head = head.next
        ng.next = None
        nl.next = hg.next
        return hl.next