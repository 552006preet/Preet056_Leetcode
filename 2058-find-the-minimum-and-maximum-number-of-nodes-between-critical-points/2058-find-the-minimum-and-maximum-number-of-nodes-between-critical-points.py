# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def isCritical(prev, curr, nxt):
            return (curr.val > prev.val and curr.val > nxt.val) or \
                   (curr.val < prev.val and curr.val < nxt.val)

        i = 1
        prev, curr, nxt = head, head.next, head.next.next
        first, last = -1, -1
        minDist = float('inf')

        while nxt:
            if isCritical(prev, curr, nxt):
                if first == -1:
                    first = i
                else:
                    minDist = min(minDist, i - last)
                last = i
            prev, curr, nxt = curr, nxt, nxt.next
            i += 1

        if first == -1 or first == last:
            return [-1, -1]
        return [minDist, last - first]