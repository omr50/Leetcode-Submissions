class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # -10 ^ 4 to 10 ^ 4
        
        # 1 1 2 2 3 4 5 5 5 
        
        # [0, 2, 2, 1, 1, 3]
        
        # [[0], [3, 4], [1, 2], [5]]
        
        # first sort the elements (bucket sort)
        
        counter = [0] * (2*10**4+1)
        
        for num in nums:
            counter[num+(10**4)] += 1
        
        counter2 = [[] for x in range(len(counter))]
        for index, count in enumerate(counter):
            counter2[count].append(index)
            
        output = []
        
        for i in range(len(counter2)):
            if counter2[-1 - i]:
                for num in counter2[-1 - i]:
                    if len(output) < k:
                        output.append(num - (10**4))
                    else:
                        return output