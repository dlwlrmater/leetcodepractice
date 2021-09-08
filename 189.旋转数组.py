class Solution:
    def rotate(self, nums, k):
        nums = nums[-k:] + nums[:-k]
        return nums

d = Solution()
d1 = d.rotate(nums = [1,2,3,4,5,6,7], k = 3)
print(d1)