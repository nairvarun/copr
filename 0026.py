# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         s = sorted(set(nums))
#         n = s + [None for _ in range(len(s))]
#         return len(n), n

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        i = 0
        for j in range(1,len(nums)):
            # if nums[j] != nums[j-1]:
            nums[i] = nums[0]
            i += 1
        nums[i] = nums[0]
        # nums = [1, 2, 3, 4, 5, 6]

        return i+1

nums = [1, 1, 2, 2, 3, 3, 4, 4, 4, 5]
print(nums)
print(Solution.removeDuplicates(Solution, nums))
print(nums)
