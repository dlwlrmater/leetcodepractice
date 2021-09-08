class Solution:
    def strStr(self, haystack, needle):
        l = len(needle)
        i = 0
        while i <= len(haystack)-l:
            # print(needle[i:i+l])
            # print(i)
            if haystack[i:i+l] == needle:
                return i
            else:
                i+=1
        return -1





d = Solution()
d1 = d.strStr('hello','ll')
print(d1)