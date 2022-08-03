class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        outPerm =[]
        
        if not nums or len(nums) ==1:
            return [nums]
        
        for i in range(len(nums)):
            dupNums = nums.copy()
            #learned something new here: python stores its values in a different way than I expected
            #just doing dupNums = nums won't create a copy, it will just use two different names
            #to point to the same list, so I have to explicitly say nums.copy() to cerate a copy
            dupNums.remove(nums[i])
            subPerm = self.permute(dupNums)
            
            for j in range(len(subPerm)):
                subPerm[j].insert(0, nums[i])
                outPerm.append(subPerm[j])
        return outPerm
    