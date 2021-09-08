# 重点
# sorted(key=functools.cmp_to_key)

class Solution:
    def largestNumber(self, nums):
        from functools import cmp_to_key
        key = cmp_to_key(lambda x,y:int(y+x)-int(x+y))
        res = ''.join(sorted(list(map(str,nums)),key=key)).lstrip('0')
        return res or '0'




d = Solution()
d1 = d.largestNumber([5,7,6,1])
# print(45,454,453)
print(d1)