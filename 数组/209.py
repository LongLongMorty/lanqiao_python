class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        a = 0
        l, r = 0, 0
        s = 0
        b = []
        while a < len(nums):
            s += nums[a]
            r += 1
            while s >= target and r != l:
                b.append(r - l)
                s -= nums[l]
                l += 1

            a += 1
        if len(b) == 0:
            return 0
        b.sort()
        return b[0]




