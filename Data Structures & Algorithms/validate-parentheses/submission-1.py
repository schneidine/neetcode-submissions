class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            ')':'(',
            ']':'[',
            '}':'{'
            }

        stack = []
        
        for c in s:
            if c in parens.values():
                stack.append(c)
            if c in parens.keys():
                if len(stack) < 1:
                    return False
                else:
                    if parens[c] == stack[-1]:
                        stack.pop()
                    else:
                        return False

        if len(stack) < 1:
            return True
        else:
            return False



