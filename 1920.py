class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[nums[i]] for i in range(len(nums))]

nums = [0,2,1,5,3,4]
print(Solution.buildArray(Solution, nums))
