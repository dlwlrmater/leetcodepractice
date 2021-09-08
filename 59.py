class Solution(object):
    def generateMatrix(self, n):
        lst = [[0]* n for _ in range(n)]
        a,b = 0,0
        for i in range(n*n):
            if b <n:
                lst[a][b] = i
                b+=1
            elif b == n-1:
                if a<n:
                    lst[a+1][b] = i
                    a +=1
            print(lst)
            print(i)



a = Solution()
b = a.generateMatrix(3)
print(b)