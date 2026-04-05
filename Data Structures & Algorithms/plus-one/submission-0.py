class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tenth = 0
        for i in range(len(digits)-1,-1,-1):
            if i==len(digits)-1:
                res = digits[i]+1+tenth
            else:
                res = digits[i]+tenth
            digits[i]=res%10
            tenth=res//10
        
        if tenth:
            return [1]+digits
        else:
            return digits