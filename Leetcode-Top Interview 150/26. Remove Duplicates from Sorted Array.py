class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i = 1
        # while True:
        #     nums[i] = nums[i]
        #     i = i + 1
        nums[1:] = (value for i, value in enumerate(nums) if nums[i] > nums[i-1])
        k = len(nums)
        return k 