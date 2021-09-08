import re
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

# 作者：QQqun902025048
# 链接：https://leetcode-cn.com/problems/string-to-integer-atoi/solution/python-1xing-zheng-ze-biao-da-shi-by-knifezhu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。