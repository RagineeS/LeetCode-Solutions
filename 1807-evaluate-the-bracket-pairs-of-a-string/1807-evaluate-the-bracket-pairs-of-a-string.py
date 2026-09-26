class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mp = {k:v for k, v in knowledge}
        result = ""
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                j = s.find(')', i + 1)
                temp = s[i + 1:j]
                result += mp.get(temp, '?')
                i = j
            else:
                result += s[i]
            i += 1

        return result