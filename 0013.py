class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        ans = vals[s[-1]]
        for i in range(len(s)-1):
            if vals[s[i]] >= vals[s[i+1]]: ans += vals[s[i]]
            else: ans -= vals[s[i]]
        return ans

# M(1000) > D(500) > C(100) > L(50) > X(10) > V(5)
s = "MDCXCV"
print(Solution.romanToInt(Solution, s))
