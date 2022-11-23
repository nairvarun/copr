class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=len)
        i = 0
        while i <= len(strs[0]):
            if not all(strs[0][:i] == x for x in map(lambda x: x[:i], strs)):
                break
            i+=1
        return strs[0][:i-1]

strs = ["flower","flow","floight"]
print(Solution.longestCommonPrefix(Solution, strs))
