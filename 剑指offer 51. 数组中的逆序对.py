# 归并排序 分而治之 递归
class Solution:
    def reversePairs(self, nums):
        size = len(nums)
        if size < 2:
            return 0
        temp = [0 for i in range(size)]
        return self.count_reverse_pairs(nums,0,size-1,temp)

    def count_reverse_pairs(self,nums,left,right,temp):
        if left == right:
            return 0
        mid = (left +right) //2
        left_pair = self.count_reverse_pairs(nums,left,mid,temp)
        right_pair = self.count_reverse_pairs(nums,mid+1,right,temp)

        reverse_pairs = left_pair + right_pair
        if nums[mid] <= nums[mid+1]:
            return reverse_pairs
        reverse_cross_pairs = self.

    def merge_and_count(self,nums,left,mid,right,temp):
        for i in range(left,right+1):
            temp[i] = nums[i]
        i = left
        j = mid + 1
        res = 0
        for k in range(left,right+1):
            if i > mid:







d = Solution()
d1 = d.reversePairs([7,5,6,4])
print(d1)