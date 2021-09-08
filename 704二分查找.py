class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right  = len(nums)-1
        while left < right:
            mid = int((left + right) / 2)
            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid
            else:
                return mid
            # print('left',left,'right',right)
        return -1

d = Solution()
d1 = d.search([-1,0,3,5,9,12],9)
print(d1)