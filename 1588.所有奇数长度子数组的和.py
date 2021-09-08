class Solution:
    def sumOddLengthSubarrays(self, arr):
        l = len(arr)
        a = 0
        for i in range(1,l+1,2):
            for j in range(l+1-i):
                a += sum(arr[j:j + i])
        return a