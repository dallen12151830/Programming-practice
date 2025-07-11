class Solution(object):
    def removeDuplicates(self, nums):
        j = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j = j + 1
        return j