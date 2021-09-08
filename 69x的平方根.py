class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x //2
        if x == 0:
            return 0
        while left < right:
            mid = (left+right+1) // 2
            print('mid',mid)
            if mid > x/mid:
                right = mid - 1
            else:
                left = mid
            print('x',x,'left',left,'right',right)
        return left

d = Solution()
d1 = d.mySqrt(7)
print(d1)