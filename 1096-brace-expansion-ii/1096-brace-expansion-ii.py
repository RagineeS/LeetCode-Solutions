class Solution:
    def getUnit(self):
        result = set()
        if self.s[self.idx] == '{':
            self.idx += 1
            result = self.performUnion()
        else:
            result = {self.s[self.idx]}
        self.idx += 1
        return result

    def performConcat(self):
        result = {""}
        while self.idx < self.n and (self.s[self.idx] == '{' or self.s[self.idx].isalpha()):
            temp = self.getUnit()
            result = {a + b for a in result for b in temp}
        return result

    def performUnion(self):
        result = set()
        while True:
            result.update(self.performConcat())
            if self.idx < self.n and self.s[self.idx] == ',':
                self.idx += 1
            else:
                break
        return result

    def braceExpansionII(self, expression):
        self.s = expression
        self.n = len(expression)
        self.idx = 0
        return sorted(self.performUnion())