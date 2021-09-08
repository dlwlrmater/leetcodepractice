class Solution:
    def search(self, nums,target):
        left = 0
        right = len(nums)-1
        if not nums:
            return -1
        while left<=right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid +1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid -1


        return -1

    # elif len(nums) == 1:
    # if nums[0] == target:
    #     return 0
    # else:
    #     return -1

d = Solution()
d1 = d.search([3,1],1)
print(d1)


