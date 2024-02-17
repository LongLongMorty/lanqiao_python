class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = 0
        while a < len(nums):
            nums[a] = nums[a] * nums[a]
            a += 1
        nums.sort()
        return nums
