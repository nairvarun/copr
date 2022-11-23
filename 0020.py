class Solution:
    def isValid(self, s: str) -> bool:
        o = []
        for i in s:
            if i == '(': o.append(1)
            elif i == '[': o.append(2)
            elif i == '{': o.append(3)
            elif len(o) == 0: return False
            elif i == ')' and not o.pop() == 1: return False
            elif i == ']' and not o.pop() == 2: return False
            elif i == '}' and not o.pop() == 3: return False
        return o == []

s = ")"
print(Solution.isValid(Solution, s))
