# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        n = 1
        nd = head
        while nd.next:
            n += 1
            nd = nd.next
        nd.next = head
        k %= n
        for _ in range(n-k):
            nd = nd.next
        res = nd.next
        nd.next = None
        return res