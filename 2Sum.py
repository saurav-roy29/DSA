class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        res = {}
        for i in range(length):
            diff = target - nums[i]
            if diff in res:
                return [res[diff], i]
            res[nums[i]] = i
        return -1



s = Solution()
nums = [2,7,11,15]
target = 9

print(s.twoSum(nums, target))
