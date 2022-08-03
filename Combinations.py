class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combArr=[]
        for i in range(1,n+1):
            combArr.append(i)
        temp=[]
        finalRes=[]
        def searchArr(m,num):
            if m==k:
                finalRes.append(temp[:])
                return
            else:
                if len(num) < (k-m):
                    return
                for i in range(len(num)):
                    temp.append(num[i])
                    searchArr(m+1,num[i+1:])
                    temp.pop()
        searchArr(0,combArr)
        return finalRes