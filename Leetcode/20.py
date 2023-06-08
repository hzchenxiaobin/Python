class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                l.append(c)
            else:
                if len(l) == 0:
                    return False
                elif c == ')':
                    if l[-1] != '(':
                        return False
                    del l[-1]
                elif c == ']':
                    if l[-1] != '[':
                        return False
                    del l[-1]
                elif c == '}':
                    if l[-1] != '{':
                        return False
                    del l[-1]
        return len(l) == 0