# 方法一：如果遇到等于val的值就用当前数组最后一个元素代替，数组大小减一
# 缺点是不能保证原来元素顺序
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                nums[i] = nums[length - 1]
                length -= 1
            else:
                i += 1
        return length


# 方法二 ：快慢指针（双指针）
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        l = length
        f, s = 0, 0
        while f < length:
            if nums[f] != val:
                nums[s] = nums[f]
                s += 1
                f += 1
            else:
                f += 1
                l -= 1

        return l
