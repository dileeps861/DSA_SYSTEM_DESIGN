class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(a, b, op):
            if op == "*":
                return a * b
            elif op == "/":
                # Ensure the division truncates towards zero
                return int(a / b) if a * b > 0 else -(abs(a) // abs(b))
            elif op == "-":
                return a - b
            else:
                return a + b

        stack = []
        operation = {"*", "/", "+", "-"}
        for token in tokens:
            if token not in operation:
                stack.append(int(token))
            else:
                b = stack.pop(-1)
                a = stack.pop(-1)
                res = calculate(a, b, token)
                print(a,token, b,"=", res)
                stack.append(res)
        print(stack)
        return stack[-1]

