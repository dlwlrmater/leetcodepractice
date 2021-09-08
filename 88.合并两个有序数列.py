class Solution:
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        c = []
        while i < m or j < n:
            # print('i',i,'j',j)
            if i == m:
                c.append(nums2[j])
                j +=1
            elif j == n:
                c.append(nums1[i])
                i +=1
            elif nums1[i] < nums2[j]:
                c.append(nums1[i])
                i +=1
            else:
                c.append(nums2[j])
                j+=1
        nums1[:] = c
        return nums1




d = Solution()
d1 = d.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
print(d1)