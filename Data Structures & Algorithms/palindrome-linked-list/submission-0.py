# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        stack = []

        while curr:
            stack.append(curr.val)
            curr = curr.next

        l, r = 0, len(stack) - 1

        while l <= r:
            if stack[l] == stack[r]:
                l += 1
                r -= 1
            else:
                return False
        return True