class Solution:
    def findMin(self, nums):
        while len(nums) > 1 and nums[0] == nums[-1]:
            nums.pop()
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                return nums[left]
            else:
                if nums[mid] == nums[left]:
                    left = left + 1
                elif nums[mid] == nums[right]:
                    right = right - 1
                else:
                    if nums[mid] <nums[right]:
                        right = mid
                    elif nums[mid] >= nums[left]:
                        left= mid+1
        return nums[left]


d = Solution()
d1 = d.findMin([1,3,5])
print(d1)