class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        arr = [-1] * n

        # Match parentheses
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                openIndex = stack.pop()
                arr[openIndex] = i
                arr[i] = openIndex

        # Traverse with direction
        res = []
        i = 0
        direction = 1

        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = arr[i]
                direction *= -1
            else:
                res.append(s[i])
            i += direction

        return "".join(res)