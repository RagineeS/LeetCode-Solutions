class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, lv = [], 0
        for c in s:
            if c == ")":
                lv -= 1
            if lv > 0:
                res.append(c)
            if c == "(":
                lv += 1
                
        return "".join(res)