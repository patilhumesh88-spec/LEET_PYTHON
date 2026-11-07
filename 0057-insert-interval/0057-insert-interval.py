class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        start1 = newInterval[0]
        end1 = newInterval[1]

        for i in range(len(intervals)):

            start2 = intervals[i][0]
            end2 = intervals[i][1]

            # Current interval is completely before new interval
            if end2 < start1:
                res.append([start2, end2])
                continue

            # Current interval is completely after new interval
            if start2 > end1:
                res.append([start1, end1])

                start1 = start2
                end1 = end2
                continue

            # Overlapping intervals
            start1 = min(start1, start2)
            end1 = max(end1, end2)

        res.append([start1, end1])

        return res

        