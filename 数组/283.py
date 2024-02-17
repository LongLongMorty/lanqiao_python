class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        fast, slow = 0, -1
        while fast < len(nums):
            if nums[fast] != 0:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
            else:
                fast += 1
                count += 1
        while count > 0:
            slow += 1
            nums[slow] = 0
            count -= 1
