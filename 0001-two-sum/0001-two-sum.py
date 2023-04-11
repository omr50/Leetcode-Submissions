class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for index, num in enumerate(nums):
            x = target - num
            if x in hashmap:
                return [hashmap[x], index]
            hashmap[num] = index
        