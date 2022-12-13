class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0 , len(nums) - 1
        i = 0
        if nums[r] > nums[l]:
            nums[l], nums[r] = nums[r], nums[l]
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            i += 1

        
        