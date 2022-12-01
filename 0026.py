# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         s = sorted(set(nums))
#         n = s + [None for _ in range(len(s))]
#         return len(n), n

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        k = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[k] = nums[i+1]
                k += 1
                continue
        return k

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(Solution, nums))
print(nums)
