class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        for j in range(len(nums)):
            return nums[k-1]

        