class Solution:
    def findDuplicate(self, nums):
        left = 0
        right = len(nums) - 1
        size = len(nums)
        while left< right:
            mid = (left + right) // 2
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt +=1
            if cnt > mid:
                right = mid
            else:
                left = mid +1
        return left




d = Solution()
d1 = d.findDuplicate([2,2,4,3,1])
print(d1)