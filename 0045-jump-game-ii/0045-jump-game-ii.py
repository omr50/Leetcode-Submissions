class Solution:
    def jump(self, nums: List[int]) -> int:
        # starting from the end either we will encounter
        # the direct path from end to front or we will
        # start off on the wrong one then encounter the right
        # one which will end up taking less steps so we replace as
        # the new minimum.
        
        # we keep all of the other jumps in the array with their minimum
        # jumps to reach maximum. And then when we move to a new index we 
        # ask, "For all indexes before this one (to the left or right depending 
        # on bottom up or top down)" if those indexes are within the jump range
        # of this current index does 1 + that other indexes minimum jumps to end
        # become the new minimum?" so we can check all previous indexes if they are
        # within jump range. If they are we can check if 1 + it will give minimum. 
        # this is a dp solution
        hashmap = {len(nums)-1:0}
        for i in range(len(nums)-2,-1,-1):
            currMin = len(nums)
            for j in range(i+1, nums[i]+i+1):
                if j in hashmap:
                    currMin = min(currMin, 1 + hashmap[j])
            hashmap[i] = currMin
        return hashmap[0]