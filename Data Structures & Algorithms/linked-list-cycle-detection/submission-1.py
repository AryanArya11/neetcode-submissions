# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        res = head
        seen.add(res)
        while res:
            res = res.next 
            if res in seen:
                return True
            seen.add(res)
        return False

        
            