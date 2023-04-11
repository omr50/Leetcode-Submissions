class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        
        def getCount(arr, word):
            for char in word:
                arr[ord(char) - ord('a')] += 1
        
        getCount(count1, s)
        getCount(count2, t)
        
        for i in range(len(count1)):
            if (count1[i] != count2[i]):
                return False
        
        return True