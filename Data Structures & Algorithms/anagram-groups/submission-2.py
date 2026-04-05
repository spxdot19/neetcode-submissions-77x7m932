class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hM = defaultdict(list)
        for i in strs:
            key = [0]*26
            for j in i:
                key[ord(j)-ord('a')]+=1
            
            hM[tuple(key)].append(i)
        
        return list(hM.values())
