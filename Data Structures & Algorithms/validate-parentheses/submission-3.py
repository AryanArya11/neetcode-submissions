class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        scan = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        for char in s:
            if char in scan:
                if stack and stack[-1] == scan[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0