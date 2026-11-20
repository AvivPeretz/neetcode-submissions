class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+","-","*","/"}
        stack = []
    
        for c in tokens:
            if c not in op:
                stack.append(int(c))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                match c:
                    case "+":
                        res = num1 + num2
                    case "-":
                        res = num1 - num2
                    case "*":
                        res = num1 * num2
                    case "/":
                        if num2 == 0: return ValueError
                        else: 
                            res = int(num1 / num2)
                stack.append(res)
        res = stack.pop()
        return res            