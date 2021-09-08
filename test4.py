class Solution:
    def findMin(self, nums):
        while len(nums) > 1 and nums[0] == nums[-1]:
            nums.pop()
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == nums[left]:
                left = left + 1
            eli f nums[mid] == nums[right]:
                right = right + 1
            else:
                if nums[left] < nums[right]:
                    return nums[left]
                else:
                    if nums[mid] > nums[left]:
                        left = mid
                    else:
                        right = mid
        return nums[mid]


d = Solution()
d1 = d.findMin([2,2,2,0,1])
print(d1)