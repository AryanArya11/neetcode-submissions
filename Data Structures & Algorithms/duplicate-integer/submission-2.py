class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for idx, num in enumerate(nums):
            if num in seen:
                return True
            seen[num] = 1
        
        return False