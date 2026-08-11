# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.stack=[]
        curr=head
        while curr:
            self.stack.append(curr.val)
            curr=curr.next
        
        curr=head
        while curr:
            if curr.val!=self.stack[-1]:
                return False
            else:
                self.stack.pop()
                curr=curr.next
        return True