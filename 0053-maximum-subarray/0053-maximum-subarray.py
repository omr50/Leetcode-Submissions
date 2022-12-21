class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        tempTotal = 0
        for i in nums:
            tempTotal += i
            total = max(tempTotal, total)
            if tempTotal < 0:
                tempTotal = 0
        return total