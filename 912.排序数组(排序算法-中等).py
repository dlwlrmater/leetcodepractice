class Solution:
    def sortArray(self, nums):
        r = 0
        l = len(nums)
        for i in range(l):
            r = i
            for j in range(i+1,l):
                if nums[r] > nums[j]:
                    r = j
            nums[i],nums[r] = nums[r],nums[i]
        return nums

d = Solution()
d1 = d.sortArray([-1,2,-8,-10])
print(d1)