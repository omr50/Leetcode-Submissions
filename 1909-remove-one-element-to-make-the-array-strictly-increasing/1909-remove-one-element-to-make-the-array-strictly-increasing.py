class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        sequence = nums
        if len(sequence) == 1:
            return True

        def recurSequence(prev, curr, skipped):
            if curr == len(sequence):
                return True
            if sequence[curr] == None:
                curr += 1
            if sequence[prev] == None:
                if curr - prev == 1:
                    prev += 1
                    curr += 1
                else:
                    prev += 1
            if curr == len(sequence):
                return True
            if sequence[prev] >= sequence[curr]:
                if skipped == True:
                    return False
                skipped = True
                temp = sequence[curr], sequence[prev]
                sequence[curr] = None
                if recurSequence(0, 1, skipped):
                    return True
                sequence[curr] = temp[0]

                sequence[prev] = None
                if recurSequence(0, 1, skipped):
                    return True
                # sequence[prev] = temp[1]
                return False

            return recurSequence(prev+1, curr+1, skipped)

        return recurSequence(0, 1, False)