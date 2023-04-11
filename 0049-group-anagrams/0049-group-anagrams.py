class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def produceCountArray(word):
            # return a tuple (array isnt hashable (mutable))
            # which contains the count of all 26 letters.
            # Therefore anagrams should have the same count
            # with an identical tuple. Can use the tuple to hash
            # them together.  key : value -> tuple : [list of anagrams]
        
            arr = [0] * 26
            
            for char in word:
                arr[ord(char) - ord('a')] += 1
            
            return tuple(arr)
        
        # hash set which has tuple mapped to list of anagrams
        hashset = {}
        for word in strs:
            currTuple = produceCountArray(word)
            if currTuple in hashset:
                hashset[currTuple].append(word)
            else:
                hashset[currTuple] = [word]
        
        return hashset.values()
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def counter1(string):  # o(n)   turning array into string takes o(n) as well but o(2n) reduces to o(n)
#             temp = [0]* 26
#             for i in string:
#                 temp[ord(i)- ord('a')] += 1
#             return str(temp)
#         dict1 = {}
#         for i in strs:  # o(m) for loop and o(n) for the counter1 so o(n*m) m is avg size of string and n is amt of strings in array
#             x = counter1(i)
#             if x in dict1:
#                 dict1[x].append(i)
#             else:
#                 dict1[x] = [i]
#         return dict1.values()
        
# # complexity is o(m*n)            
    
    
    
    
    
    
    
    
# working soltion but m*nlog(n) we can do better    
# def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         dict1 = {}
#         for i in strs:
#             x = str(sorted(i))
#             if x in dict1:
#                 dict1[x].append(i)
#             else:
#                 dict1[x] = [i]
                
# # this above makes all elements that are the same when sorted (anagrams) grouped together in their unsorted form
#         return [dict1[x] for x in dict1] 