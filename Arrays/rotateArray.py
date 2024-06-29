class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k=k%length
        start = 0
        end = length-1

        #  reverse the entire string
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1

        # reverse first half of string
        start, end = 0, k-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end -=1

        #  reverse the second half of the string
        start, end = k, length-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        
