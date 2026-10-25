class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops = {'+', 'C', 'D'}

        for i in operations:
            # need to check whether num is int:
            if i in ops:
                if i == '+':
                    new = stack[-1] + stack[-2]
                    stack.append(new)
                elif i == 'C':
                    stack.pop()
                elif i == 'D':
                    new = stack[-1] * 2
                    stack.append(new)
            
            else:
                stack.append(int(i))
                
        return sum(stack)