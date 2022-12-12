class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        if len(s) == 1 or len(s) == 0:
            if s == t:
                return s
            else:
                return ''
        hashmap = {}
        for i in t:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        newS = []
        for i in range(len(s)):
            if s[i] in hashmap:
                newS.append((s[i], i))
        if not newS or len(newS) < len(t):
            return ''
        foundSet = set(hashmap)
        l, r = 0, 1
        if len(newS) == 1:
            if newS[0][0] == t:
                return t
            else:
                return ''
        hashmap[newS[l][0]] -= 1
        hashmap[newS[r][0]] -= 1
        if hashmap[newS[l][0]] <= 0:
            foundSet.remove(newS[l][0])
        if hashmap[newS[r][0]] <= 0:
            if newS[r][0] in foundSet:
                foundSet.remove(newS[r][0])
        minStr = ''
        minimum = float('inf')
        while r < len(newS):
            if not foundSet: # found (confusing name tho)
                hashmap[newS[l][0]] += 1
                if hashmap[newS[l][0]] > 0:
                    foundSet.add(newS[l][0])
                if newS[r][1] - newS[l][1] + 1 < minimum:
                    minStr = s[newS[l][1]: newS[r][1]+1]
                    minimum = newS[r][1] - newS[l][1] + 1
                l += 1
            else: # not found
                r += 1
                if r < len(newS):
                    hashmap[newS[r][0]] -= 1
                    if hashmap[newS[r][0]] <= 0:
                        if newS[r][0] in foundSet:
                            foundSet.remove(newS[r][0])
                else: # probably unessecary because it breaks on next iteration of while loop 
                    break
        if minimum == float('inf'):
            return ''
        return minStr