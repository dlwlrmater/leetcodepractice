class Solution:
    def removeElement(self, nums, val):
        left = 0
        right = len(nums)
        for i in range(right):
            if nums[i] != val:
                nums[left] = nums[i]
                left +=1
        return left

d = Solution()
d1 = d.removeElement([3,2,2,3],3)
print(d1)