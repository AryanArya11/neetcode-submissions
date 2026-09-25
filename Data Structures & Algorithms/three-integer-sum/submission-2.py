class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()


        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
    
            a, b = i + 1, len(nums) - 1
            while a < b:
                threeSum = nums[i] + nums[a] + nums[b]

                if threeSum > 0:
                    b -= 1
                elif threeSum < 0:
                    a += 1
                else:
                    res.append([nums[i], nums[a], nums[b]])
                    a += 1
                    b -= 1
                    while nums[a] == nums[a - 1] and a < b:
                        a += 1
        return res

            


