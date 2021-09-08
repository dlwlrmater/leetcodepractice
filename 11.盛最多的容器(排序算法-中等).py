class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        s = 0
        if len(height) >2:
            for i in range(len(height)-1):
                r = min(height[left],height[right]) * (right-left)
                # print('left',left)
                # print('right',right)
                # print(r)
                if r > s:
                    s = r
                if height[left] <= height[right]:
                    left+=1
                else:
                    right -=1
            return s
        else:
            return min(height)*1
        



d = Solution()
d1 = d.maxArea([1,1])
print(d1)