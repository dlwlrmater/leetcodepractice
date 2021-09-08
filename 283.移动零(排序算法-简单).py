class Solution:
    def moveZeroes(self, nums):
        a = 0
        b = 0
        while a < len(nums) - 1:
            if nums[a] == 0:
                pass
            else:
                b += 1
            a += 1
            nums[b] = nums[a]
            print(nums)
        for i in range(b + 1, a + 1):
            nums[i] = 0
        return nums


d = Solution()
d1 = d.moveZeroes([0,0,1])
print(d1)
