class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDup = {}
        for i in nums:
            numDup[i]=0
        for i in nums:
            numDup[i]+=1
        for i in numDup:
            if numDup[i] > 1:
                return True
        return False