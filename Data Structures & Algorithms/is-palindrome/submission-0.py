class Solution:
    def isPalindrome(self, s: str) -> bool:
        sWW = ""
        for i in s:
            if i!=" " and i.isalnum(): sWW+=i
        
        sWW = sWW.lower()
        print(sWW)
        Hlength = len(sWW)//2
        for i in range(Hlength):
            print(sWW[i],sWW[len(sWW)-1-i])
            if sWW[i] != sWW[len(sWW)-1-i]: return False
        return True
