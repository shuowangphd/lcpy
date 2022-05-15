# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        fh = ListNode(next = head)
        nd = fh
        for _ in range(left-1):
            nd = nd.next
        n1 = nd
        n2 = nd.next
        nd = nd.next
        nd3 = nd.next
        for _ in range(right-left-1):
            nd,nd3.next,nd3 = nd3,nd,nd3.next
        n2.next = nd3.next
        nd3.next = nd
        n1.next = nd3
        return fh.next