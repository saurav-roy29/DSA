class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        res = set()
        for i in range(length):
            if nums[i] in res:
                return True
            else:
                res.add(nums[i])
        else:
            return False
