class Solution:
    def isHappy(self, n: int) -> bool:
        hM = defaultdict(int)
        num = n
        res = 0
        while True:
            print(hM)
            for i in str(num):
                j = int(i)
                res+=(j**2)
            if res==1:
                return True
            if hM[res]==1:
                return False
            hM[res] = 1
            num = res
            res = 0

        

