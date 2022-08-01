class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq as hp
        hp.heapify(nums)
        return hp.nlargest(k,nums)[-1]