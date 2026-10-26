# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        from itertools import count

        heap = []
        unique = count()

        for list in lists:
            if list:
                heapq.heappush(heap, (list.val, next(unique), list))
        
        dummy = ListNode(0)
        current = dummy

        while heap:
            _, _, node = heapq.heappop(heap)

            current.next = node
            current = node

            if node.next:
                heapq.heappush(heap, (node.next.val, next(unique), node.next))

        return dummy.next