# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nd = head
        while nd and nd.next:
            if nd.val == nd.next.val:
                nd.next = nd.next.next
            else:
                nd = nd.next
        return head