class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        output = []
        while i < len(nums):
            
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    output.append([nums[i], nums[j] , nums[k]])
                    prev = k
                    while k > j and nums[k] == nums[prev]:
                        k -= 1
                    prev = j
                    while j < k and nums[j] == nums[prev]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    prev = k
                    while k > j and nums[k] == nums[prev]:
                        k -= 1
                else:
                    prev = j
                    while j < k and nums[j] == nums[prev]:
                        j += 1
            prev = i
            while i < len(nums) and nums[i] == nums[prev]:
                i += 1
        return output