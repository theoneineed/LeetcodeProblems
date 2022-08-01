class Solution:
    def isHappy(self, n: int) -> bool:
        sumv = 0
        vis = []
        vis.append(n)

        while sumv != 1:
            while n !=0:
                sumv += (n%10)**2
                n= int(n/10)
            n = sumv            
            print(sumv)
            if sumv == 1:
                return True
            if sumv in vis:
                return False
            vis.append(sumv)
            sumv = 0
        return True