class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[left] < nums[right]:
                return nums[left]
            else:
                if nums[mid]>=nums[left]:
                    left = mid + 1
                    print('azz')
                elif nums[mid] < nums[right]:
                    right = mid -1
            print(left,right,mid)
        return nums[left]

d = Solution()
d1 = d.findMin([2,1])
print(d1)