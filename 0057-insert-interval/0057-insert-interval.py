class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        output = []
        added = False
        for i in range(len(intervals)):
            if (intervals[i][0] <= newInterval[0] <= intervals[i][1] or intervals[i][0] <= newInterval[1] <= intervals[i][1] or (newInterval[0] <= intervals[i][0] and newInterval[1] >= intervals[i][1]) or (intervals[i][0] <= newInterval[0] and intervals[i][1] >= newInterval[1])):
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            elif newInterval[1] < intervals[i][0]:
                if not added:
                    added = True
                    output.append(newInterval)
                output.append(intervals[i])
            else:
                output.append(intervals[i])
        if not added:
            output.append(newInterval)
        return output