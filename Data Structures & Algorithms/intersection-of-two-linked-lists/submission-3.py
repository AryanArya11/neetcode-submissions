# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA, listB = headA, headB
        seen = set()

        while listA:
            seen.add(listA)
            listA = listA.next
        
        while listB:
            if listB in seen:
                return listB
            listB = listB.next
        return None