class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # import heapq as hp
        # hp.heapify(nums)
        for count, item in enumerate(nums):
            if item == target:
                return count
            elif item < target:
                continue
            else:
                return count
        return count+1
            
         