class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        return [sum(nums[:i]) for i in range(1, len(nums) + 1)]

nums = [1,2,3,4]
print(Solution.runningSum(Solution, nums))
