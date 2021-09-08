class Solution:
    def findBestValue(self, arr, target):
        l = len(arr)
        avgg =  target/l
        print(avgg)
        a = 0
        b = 0
        for i in arr:
            if i < avgg:
                b +=i
                a += 1

        re = (target-b)//(l-a)
        if re*(l-a)+b-target < (re-1)*(l-a)+b-target:
            return re+1
        else:
            return re





d = Solution()
# d1 = d.findBestValue([4,9,3],10)
d1 = d.findBestValue([60864,25176,27249,21296,20204],56803)
# print(round(15.5,0))
print(d1)