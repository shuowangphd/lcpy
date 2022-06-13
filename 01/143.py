# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return []
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow.next
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex    
        slow.next = None
        
        head1, head2 = head, prev
        while head2:
            nex = head1.next
            head1.next = head2
            head1 = head2
            head2 = nex