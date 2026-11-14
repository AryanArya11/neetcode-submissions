# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        head1, head2 = headA, headB

        seen = set()

        while head1:
            seen.add(head1)
            head1 = head1.next

        while head2:
            if head2 in seen:
                return head2
            head2 = head2.next
        return None
