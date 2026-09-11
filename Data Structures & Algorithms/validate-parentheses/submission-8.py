class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        scan = {
            ')' : '(',
            ']' :  '[',
            '}' : '{'
        }

        for idx, i in enumerate(s):
            if i in scan:
                if stack and stack[-1] == scan[i]:
                    stack.pop()
                else:
                    return False        
            else:
                stack.append(i)
    
        return len(stack) == 0 