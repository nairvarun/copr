# # O(n²)
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(0, len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        vals = {}
        for k, v in enumerate(nums):
            if target - v in vals:
                return [vals[target-v], k]
            else:
                vals[v] = k

nums = [2,7,11,15]
target = 9
print(Solution.twoSum(Solution, nums, target))
