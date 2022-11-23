class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        if sx == ''.join(reversed(sx)):
            return True
        else:
            return False

x = 121
Solution.isPalindrome(Solution, x)
