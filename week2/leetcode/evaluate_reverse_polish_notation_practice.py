class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []

        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                top = stack.pop()
                second_from_top = stack.pop()
                stack.append(second_from_top - top)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                top = stack.pop()
                second_from_top = stack.pop()
                # Perform integer division and handle negative numbers correctly
                result = int(second_from_top / top)
                if result < 0 and second_from_top % top != 0:
                    result += 1
                stack.append(result)
            else:
                stack.append(int(token))
            
        return stack.pop()
