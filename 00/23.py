# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        q = PriorityQueue()
        for i, node in enumerate(lists):
            if node: q.put((node.val, i, node))
        while q.qsize():
            poped = q.get()
            curr.next,i = poped[2],poped[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val,i, curr.next))
        return dummy.next