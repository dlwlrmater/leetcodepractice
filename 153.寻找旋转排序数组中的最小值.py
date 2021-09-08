class Solution:
    def findMin(self, nums):
        i = 0
        while i < len(nums)-1:
            if nums[i] > nums[i+1]:
                return nums[i+1]
            i +=1
        return nums[0]
d = Solution()
d1 = d.findMin([3,4,5,1,2])
print(d1)