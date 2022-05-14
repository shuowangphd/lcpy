# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = fh = ListNode(next = head)
        while head and head.next:
            head = head.next
            if l.next.val == head.val:
                while head and l.next.val == head.val:
                    head = head.next
                l.next = head
            else:
                l = l.next 
        return fh.next