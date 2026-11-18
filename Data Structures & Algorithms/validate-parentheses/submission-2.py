class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { '[':']', '(':')', '{':'}' }
        stack = []

        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack: return False
                if pairs[stack[-1]] == c:
                    stack.pop()
                else: return False
        return not stack

'''
define algorithm using stack:
1. set pairs to a dict of valid parentheses pairs
2. initiatalize an empty stack
3. for each char c in s:
        if c in pairs:
            check if stack is not empty and stack last element is the corresponding pair
                remove c using stack.pop
            add c to the stack
    return not stack

'''