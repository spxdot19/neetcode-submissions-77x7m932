class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        stack = [] 
        n = len(nums)
        for i in range(n):
            l = i+1
            r = n-1
            while l<r :
                aim = -nums[i]
                subStack = [nums[i],nums[l],nums[r]]
                if sum(subStack)==0 and subStack not in stack:
                    stack.append(subStack)
                else:
                    if aim > nums[l] + nums[r]:
                        l+=1
                    else:
                        r-=1
        return stack
                    



