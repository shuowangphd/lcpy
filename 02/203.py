# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        dh = ListNode()
        dh.next = head
        hd = dh
        while hd.next:
            if hd.next.val == val:
                hd.next = hd.next.next
            else:
                hd = hd.next
        return dh.next