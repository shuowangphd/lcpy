# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        while curr:
            cnxt = curr.next
            prv, nxt = dummy, dummy.next
            while nxt:
                if nxt.val > curr.val: break
                prv = nxt
                nxt = nxt.next    
            curr.next = nxt
            prv.next = curr
            curr = cnxt
        return dummy.next