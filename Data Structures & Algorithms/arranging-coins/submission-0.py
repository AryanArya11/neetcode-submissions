class Solution:
    def arrangeCoins(self, n: int) -> int:

        total = n
        
        for i in range(1, n+1):
            total -= i

            if i >= total:
                return i